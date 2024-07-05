from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewset, ProductViewset

app_name = 'api'
 #User = get_user_model()

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewset, basename='categories')
router_v1.register('products', ProductViewset, basename='products')

urlpatterns = [
    path('', include(router_v1.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
