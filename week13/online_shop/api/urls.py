from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductCreateView


urlpatterns = [
    path('product/', ProductCreateView.as_view()),
]

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')


urlpatterns += router.urls
