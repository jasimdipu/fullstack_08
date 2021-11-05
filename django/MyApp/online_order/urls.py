from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.about, name='about'),
    path("order/", views.order, name='order'),
    path("order-list/", views.order_list, name='order-list'),
    path("show_category/{str:pk}", views.show_category, name="show_category"),
]
# django-admin startapp online_order
