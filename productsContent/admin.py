from django.contrib import admin
from .models import Products, Brand, Image, Shoe_size


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand','model_name')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Shoe_size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
