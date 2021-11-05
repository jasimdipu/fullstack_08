from django.shortcuts import render, redirect
from .models import Category, Product, Order, Customer
from .forms import OrderForms


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

    print(category)

    return render(request, "category_details.html", context=context)


def about(request):
    return render(request, "about.html")


def order(request):
    form = OrderForms()

    if request.method == "POST":
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')

    context = {
        "forms": form,
    }
    return render(request, "order.html", context=context)


def order_list(request):
    order_lists = Order.objects.all()

    context = {
        'orders': order_lists
    }

    return render(request, "orderlist.html", context=context)
