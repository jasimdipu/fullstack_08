from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Customer, Product, Order


# Create your views here.


def index(request):
    # sql = select * from categories

    # orm -> object relational mapping

    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "index.html", context=context)


def show_category(request, pk):
    category = Category.objects.get(id=pk)

    context = {
        "category": category,
    }

    return render(request, "category_details.html", context=context)


def about(request):
    return render(request, "about.html")


def order(request):
    return render(request, "order.html")


def order_list(request):
    return render(request, "orderlist.html")
