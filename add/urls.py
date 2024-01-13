from django.urls import path,include
from add.views import *
urlpatterns = [
    path('category/',CategoryGenericView.as_view()),
    path('product/',AdsGenericView.as_view()),
    path('orderitem/',OrderItemGenericView.as_view()),
    path('orderitem_detail/',OrderItemDetailGenericView.as_view()),
    path('order/',OrderGenericView.as_view()),
    path('order_detail/',OrderDetailGenericView.as_view())

]