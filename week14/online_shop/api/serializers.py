from rest_framework import serializers

from .models import Item, Product, Service, Offer, ShopStore
from .models import Order, ProductOrder, ServiceOrder


# example of serializers.Serializer
class ProductSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    color = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=10)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price')


# short serializer for list products
class ProductShortSerializer(serializers.ModelSerializer):
    shop_id = serializers.IntegerField(write_only=True)
    shop_name = serializers.CharField(source='shop.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'shop_id', 'shop_name')


class ShopStoreSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(default=0)
    product_min_price = serializers.IntegerField(default=0)
    product_max_price = serializers.IntegerField(default=0)
    products = ProductShortSerializer(many=True, read_only=True)

    class Meta:
        model = ShopStore
        fields = '__all__'


# serializer for retrieve, update methods of products
class ProductFullSerializer(ProductShortSerializer):
    class Meta(ProductShortSerializer.Meta):
        fields = ProductShortSerializer.Meta.fields + ('description', 'size', 'color')


# serializer of service that inherits item serializer
class ServiceSerializer(ItemSerializer):
    class Meta(ItemSerializer.Meta):
        model = Service
        fields = ItemSerializer.Meta.fields + ('duration', )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'discount', 'price')


class ProductOrderSerializer(OrderSerializer):
    item = ProductFullSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)

    class Meta(OrderSerializer.Meta):
        model = ProductOrder
        fields = OrderSerializer.Meta.fields + ('item', 'item_id', 'quantity')


class ServiceOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    discount = serializers.IntegerField()
    price = serializers.IntegerField()
    item_id = serializers.IntegerField(write_only=True)
    item = ServiceSerializer(read_only=True)

    def create(self, validated_data):
        service_order = ServiceOrder.objects.create(**validated_data)
        return service_order

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.save()
        return instance


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('title', )

