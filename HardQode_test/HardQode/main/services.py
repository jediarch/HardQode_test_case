"""Обращения к базе данных"""
from .models import Product_Permission, Product, Lesson

def get_all_objects(model):
    return model.objects.all()

def get_allowed_list(user):
    for product_permission in Product_Permission.objects.all():
        if product_permission.user == user:
            return Product_Permission.objects.get(user=user).product.all()


def get_lessons(product_list):
    list = []
    for product in product_list:
        list.append(Lesson.objects.get(products=product))
    return list
