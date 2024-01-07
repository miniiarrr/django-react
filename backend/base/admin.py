from django.contrib import admin
from .models import Product, Review, Order, OrderItem, ShippingAddress


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'price',
        'countInStock',
        'rating',
        'numReviews',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'name',
        'rating',
        'comment',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'paymentMethod',
        'taxPrice',
        'shippingPrice',
        'totalPrice',
        'isPaid',
        'paidAt',
        'isDelivered',
        'deliveredAt',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'name',
        'qty',
        'price',
        'image',
    )


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'address',
        'city',
        'postalCode',
        'country',
    )
