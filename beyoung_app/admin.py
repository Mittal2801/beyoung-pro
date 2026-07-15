from django.contrib import admin
from .models import Category, Brand, Product, order

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(order)
# admin.site.register(Cart_Item)
