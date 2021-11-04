from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, max_length=10, decimal_places=2)
    category_id = models.ForeignKey(Category, null=True, blank=True, related_name='category', on_delete=models.SET_NULL)
    product_quantity = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    delivery_status = (
        ("Pending", "Pending"),
        ("Out of Delivery", "Out of Delivery"),
        ("Delivered", "Delivered"),
    )

    customer_id = models.ForeignKey(Customer, null=True, blank=True, related_name='customer', on_delete=models.SET_NULL)
    product_id = models.ForeignKey(Product, null=True, blank=True, related_name='product', on_delete=models.SET_NULL)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    delivery = models.CharField(max_length=100, null=True, blank=True, choices=delivery_status)

    def __str__(self):
        return self.customer_id.name+" "+self.product_id.product_name
