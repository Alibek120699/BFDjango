from rest_framework import serializers

from .models import OnlineProduct, OfflineProduct, BaseProduct


class BaseProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    # price = serializers.IntegerField()
    # desc = serializers.CharField()
    # count = serializers.IntegerField()
    # created_at = serializers.DateTimeField()

    class Meta:
        model = BaseProduct
        fields = ('price', 'desc', 'count')


class OnlineProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    price = serializers.IntegerField()
    desc = serializers.CharField()
    count = serializers.IntegerField()
    needs_delivery = serializers.BooleanField()
    delivery_address = serializers.CharField()
    delivery_price = serializers.IntegerField()

    def create(self, validated_data):
        product = OnlineProduct.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.name = validated_data.get('name', instance.name)
        instance.count = validated_data.get('count', instance.count)
        instance.delivery_address = validated_data.get('delivery_address', instance.delivery_address)
        instance.delivery_price = validated_data.get('delivery_price', instance.delivery_price)
        instance.save()
        return instance

    def validate_price(self, price):
        if price >= 50000:
            raise serializers.ValidationError('Price should be less than 50000!')
        return price


class OfflineProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = BaseProductSerializer.Meta.fields + ('discount',)
