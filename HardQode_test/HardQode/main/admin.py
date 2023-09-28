from django.contrib import admin

from .models import Product, Lesson, Product_Permission

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Product_Permission)
# Register your models here.
