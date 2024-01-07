from django.contrib import admin
from .models import Product, Review


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

