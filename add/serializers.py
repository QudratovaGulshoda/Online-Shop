from add.models import Ad, Category, OrderItem
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'user',
        )

class AdsSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True,read_only=True)
    class Meta:
        model = Ad
        fields = (
            'name',
            'image',
            'content',
            'price',
            'status',
            'categories',
        )
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'all_products',
            'all_price',
            'user'
        )
        read_only_fields = ('id',)

class OrderItemSerializer(serializers.ModelSerializer):
    baskets = OrderSerializer(many=True,read_only=True)
    class Meta:
        model = OrderItem
        fields = (
            'baskets',
            'product',
            'quantity',
            'narx',
            'xaridnarx'
        )
        read_only_fields = ('id',)