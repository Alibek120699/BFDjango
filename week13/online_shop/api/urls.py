from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ProductCreateView
from .fbv import service_order, service_order_detail


urlpatterns = [
    path('product/', ProductCreateView.as_view()),
    path('services/', service_order),
    path('services/<int:pk>/', service_order_detail),
]

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')


urlpatterns += router.urls
