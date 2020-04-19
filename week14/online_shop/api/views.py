import logging

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Product
from .serializers import ProductShortSerializer, ProductFullSerializer
from .permissions import IsAllowedToCreateProduct


logger = logging.getLogger(__name__)


class ProductCreateView(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    http_method_names = ['post']
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
    permission_classes = (IsAllowedToCreateProduct, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'Product object with {serializer.instance.id} id created')
        logger.info(f'Product object with {serializer.instance.id} id created')
        logger.warning(f'Product object with {serializer.instance.id} id created')
        logger.error(f'Product object with {serializer.instance.id} id created')
        logger.critical(f'Product object with {serializer.instance.id} id created')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False)
    def top_three_cheapest(self, request):
        queryset = Product.objects.order_by('price')[:3]
        serializer = ProductShortSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductFullSerializer(data=request.data)
        if serializer.is_valid():
            Product.objects.create(**serializer.validated_data)
            return Response(serializer.data)


    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductShortSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductFullSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Product.objects.all()


    def destroy(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        # logger.debug(f'Product object with {instance.id} id was deleted')
        # logger.info(f'Product object with {instance.id} id was deleted')
        logger.warning(f'Product object with {instance.id} id was deleted')
        logger.error(f'Product object with {instance.id} id was deleted')
        logger.critical(f'Product object with {instance.id} id was deleted')
        instance.delete()



