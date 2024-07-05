from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.serializers import ProductSerializer
from products.models import Product


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('subcategory').all()
    serializer_class = ProductSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ('subcategory', 'in_stock', 'subcategory__categories')
    search_fields = ('name',)
    ordering_fields = ('unit_price', 'discount')
