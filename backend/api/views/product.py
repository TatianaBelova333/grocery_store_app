from django.db.models import Case, F, When, DecimalField, OuterRef
from django.db import DatabaseError, transaction
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import CartItemCreateUpdateSerializer, ProductSerializer
from users.models import CartItem
from products.models import Product


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ('subcategory', 'subcategory__categories')
    search_fields = ('name', 'description')
    ordering_fields = ('unit_price', 'discount', 'created')

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_anonymous:
            user_cart_items = []

        else:
            user_cart_items = current_user.shopping_cart.items.values(
                'product'
            )

        queryset = Product.objects.filter(stock_quantity__gt=0).select_related(
            'subcategory', 'country', 'brand'
        ).annotate(
            in_cart=Case(
                When(
                    id__in=user_cart_items,
                    then=True,
                ),
                default=False,
            )
        ).annotate(
            discounted_price=F('unit_price') * (100 - F('discount')) / 100
        ).annotate(
            qty_in_cart=Case(
                When(
                    id__in=user_cart_items,
                    then=current_user.shopping_cart.items.filter(
                        product=OuterRef('id')
                    ).values('quantity')
                ),
                default=0.00,
                output_field=DecimalField()
            ))

        return queryset

    def get_serializer_class(self):
        if self.action == 'to_cart':
            return CartItemCreateUpdateSerializer
        return self.serializer_class

    @action(['post', 'delete', 'patch'],
            detail=True,
            permission_classes=[IsAuthenticated])
    def to_cart(self, request, *args, **kwargs):
        product = self.get_object()
        current_user = self.request.user
        shopping_cart = current_user.shopping_cart
        cart_item = CartItem.objects.filter(
                product=product,
                shopping_cart=request.user.shopping_cart
            )
        if request.method == 'POST':
            if cart_item.exists():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'errors': 'Данный товар уже в корзине',
                    })

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save(
                shopping_cart=shopping_cart,
                product=product
            )
            return Response(
                status=status.HTTP_201_CREATED,
                data='Товар добавлен в корзину',
            )

        if request.method == 'DELETE':
            if cart_item.exists():
                try:
                    with transaction.atomic():
                        cart_item.delete()
                        shopping_cart.updated = timezone.now()
                        shopping_cart.save()

                except DatabaseError:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={'errors': 'Ошибка удаления товара'},
                    )
                return Response(
                    status=status.HTTP_204_NO_CONTENT,
                    data='Товар удален из корзины.',
                )
            return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={'errors': 'Данного товара нет в корзине.'},
                )

        if request.method == 'PATCH':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            if cart_item.exists():
                try:
                    with transaction.atomic():
                        cart_item.update(
                            quantity=self.request.data['quantity']
                        )
                        shopping_cart = cart_item.first().shopping_cart
                        shopping_cart.updated = timezone.now()
                        shopping_cart.save()
                except DatabaseError:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={'errors': 'Ошибка изменения количества товара'},
                    )
                return Response(
                    status=status.HTTP_200_OK,
                    data='Кол-во товара изменено.',
                )

            return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={'errors': 'Данного товара нет в корзине.'},
                )
