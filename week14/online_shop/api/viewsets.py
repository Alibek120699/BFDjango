import logging

from django.db.models import Avg, Max, Min, Sum, Count
from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Product, ShopStore
from .serializers import ProductShortSerializer, ProductFullSerializer, ShopStoreSerializer


logger = logging.getLogger(__name__)


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopStoreSerializer

    def get_queryset(self):
        if self.action == 'list':
            return ShopStore.objects.prefetch_related('products')
        return ShopStore.objects.all()


class ProductModelViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Product.objects.select_related('shop')
        return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductShortSerializer
        return ProductFullSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Product object with {serializer.instance.id} id created')
        logger.info(f'Product object with {serializer.instance.id} id created')
        logger.warning(f'Product object with {serializer.instance.id} id created')
        logger.error(f'Product object with {serializer.instance.id} id created')
        logger.critical(f'Product object with {serializer.instance.id} id created')

    @action(methods=['GET'], detail=False)
    def price_report(self, request):
        data = [
            Product.objects.aggregate(Avg('price')),
            Product.objects.aggregate(Max('price')),
            Product.objects.aggregate(min_price=Min('price')),
            Product.objects.aggregate(Sum('price')),
            ShopStore.objects.values('id').annotate(Count('products')),
        ]
        return Response(data)
