from django.contrib import admin

# Register your models here.
from add.models import Category, Ad, OrderItem, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','user',)
    list_filter = ('name',)
    list_per_page = 10
    search_fields = ('name',)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Ad)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('picture','name','price','status','user')
    list_filter = ('price','created_at')
    list_editable = ('price','status',)
    search_fields = ('name',)
    list_per_page = 10

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['product','quantity','narx','xaridnarx']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['user','all_products','all_price']