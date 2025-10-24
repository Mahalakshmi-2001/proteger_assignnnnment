from rest_framework import routers
from django.urls import path,include

from .views import  AssetsViewSet,Assetpdf

router = routers.DefaultRouter()
router.register('assets',AssetsViewSet,basename='assets')

urlpatterns = [
    path('', include(router.urls)),
    path('assets_pdf/', Assetpdf.as_view(), name='assets_pdf')]