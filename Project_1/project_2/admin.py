from django.contrib import admin

# Register your models here.
from project_2.models import Category, Good, Products

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Products)

from shopping.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)