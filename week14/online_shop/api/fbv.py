from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ServiceOrder
from .serializers import ServiceOrderSerializer
from .constants import SALESMAN


@api_view(['GET', 'POST'])
def service_order(request):
    if request.user.role == SALESMAN:
        return Response({'error': 'salesman can not create order'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'GET':
        orders = ServiceOrder.objects.all()
        serializer = ServiceOrderSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ServiceOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    return Response({'error': 'bad request'})


@api_view(['GET', 'PUT', 'DELETE'])
def service_order_detail(request, pk):
    try:
        order = ServiceOrder.objects.get(id=pk)
    except ServiceOrder.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ServiceOrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'})
