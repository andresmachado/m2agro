from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns



router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]
