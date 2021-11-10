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
        "form": form,
    }
    return render(request, "order.html", context=context)


def order_list(request):
    order_lists = Order.objects.all()

    context = {
        'orders': order_lists
    }

    return render(request, "orderlist.html", context=context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForms(instance=order)

    if request.method == 'POST':
        form = OrderForms(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order-list')

    context = {
        'form': form
    }
    return render(request, 'order.html', context=context)


def show_order(request, pk):
    order_details = Order.objects.get(id=pk)

    context = {
        'order': order_details,
    }

    return render(request, 'order_details.html', context=context)


def delete_order(request, pk):
    item = Order.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('order-list')

    context = {
        'item': item,
    }

    return render(request, 'delete.html', context=context)
