from rest_framework import status, viewsets
from api.serializers import CategorySerializer

from category.models import Category


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.prefetch_related('subcategories').all()
    serializer_class = CategorySerializer
