from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path("about/", views.about, name='about'),
    path("order/", views.order, name='order'),
    path("order-list/", views.order_list, name='order-list'),
    path("category-details/{int:pk}/", views.show_category, name='category-details'),
]
# django-admin startapp online_order
