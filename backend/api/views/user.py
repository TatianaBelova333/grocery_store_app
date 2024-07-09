from django.contrib.auth import get_user_model
from django.db import DatabaseError, transaction
from django.core.exceptions import ValidationError
from djoser.conf import settings
from django.utils import timezone
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import ShoppingCart


User = get_user_model()


class CustomUserViewSet(DjoserUserViewSet):
    """
    Extends the Djoser UserViewSet.

    Additional endpoints:

    cart:
    Get or clear the request user's cart.

    """
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'cart':
            return settings.SERIALIZERS.cart
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        if self.action == 'cart':
            queryset = ShoppingCart.objects.filter(
                user=user
            ).prefetch_related('items').first()
            return queryset

        return super().get_queryset()

    @action(["get", "delete", 'patch'],
            detail=False,
            permission_classes=[IsAuthenticated])
    def cart(self, request, *args, **kwargs):

        if request.method == "GET":
            serializer = self.get_serializer(self.get_queryset())
            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        if request.method == "DELETE":
            try:
                with transaction.atomic():
                    shopping_cart = self.request.user.shopping_cart
                    shopping_cart.items.all().delete()
                    shopping_cart.updated = timezone.now()
                    shopping_cart.save()
                    serializer = self.get_serializer(self.get_queryset())

            except DatabaseError:
                raise ValidationError(
                     'Ошибка очистка корзины.'
                    )
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=serializer.data,
            )
        if request.method == "PATCH":
            pass
