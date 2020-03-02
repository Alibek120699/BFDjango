from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import OnlineProductViewSet, OfflineProductViewSet, OnlineProductCreateView


urlpatterns = [
    path('online_products/', OnlineProductCreateView.as_view()),
]

router = DefaultRouter()
router.register('offline_products', OfflineProductViewSet, basename='offline_products')
router.register('online_products', OnlineProductViewSet, basename='online_products')

urlpatterns += router.urls
