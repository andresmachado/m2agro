from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, base_name='Product')
router.register(r'harvests', views.HarvestViewSet, base_name='Harvest')
router.register(r'services', views.ServiceViewSet, base_name='Service')

urlpatterns = [
    url(r'^', include(router.urls)),
]