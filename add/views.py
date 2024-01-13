from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from add.models import *
from add.serializers import *
from rest_framework.filters import SearchFilter

class CategoryGenericView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ('name',)

class AdsGenericView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsSerializer
    filter_backends = [SearchFilter]
    search_fields = ('name','category','price',)

class OrderItemGenericView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [SearchFilter]

class OrderItemDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [SearchFilter]

class OrderGenericView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]

class OrderDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]
