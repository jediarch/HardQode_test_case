from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Lesson, Product_Permission
from .services import get_all_objects, get_allowed_list, get_lessons
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("This is the index page")

def products(request):
    product_list = get_all_objects(Product)
    context = {
        'product_list': product_list,
    }
    return render(request, 'products.html', context=context)

def details(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product_title = product.title
    description = product.description
    lessons_list = Lesson.objects.filter(products=product)

    context = {
        'product_title': product_title,
        'description': description,
        'lessons_list': lessons_list,
    }
    return render(request, 'details.html', context=context)

def lesson(request, lesson_id):
    user = request.user
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    context = {
        'user': user,
        'video_url': lesson.video_url
    }

    return render(request, 'lesson.html', context=context)


def available_products(request):
    user = request.user
    available_products_list = get_allowed_list(user)
    lessons_list = get_lessons(available_products_list)
    context = {
        'user': user,
        'available_products_list': available_products_list,
        'lessons_list': lessons_list,
    }
    return render(request, 'available_products.html', context=context)


# Create your views here.
