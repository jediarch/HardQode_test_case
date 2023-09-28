from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("products/", views.products, name='products'),
    path("products/<int:product_id>/details/", views.details, name='details'),
    path("lessons/<int:lesson_id>/", views.lesson, name='lesson'),
    path("user/", views.available_products, name='available_products'),
]