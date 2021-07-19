from django.db import models
from django.contrib.auth.models import User


class RegisterModel(models.Model):
    Name=models.CharField(max_length=30)
    Username=models.CharField(max_length=30, unique=True)
    Email=models.EmailField(max_length=20, unique=True)
    Contact=models.IntegerField()
    Address = models.CharField(max_length=120, null=True, blank=True)
    Joined_on = models.DateTimeField(auto_now_add=True)
    Password=models.CharField(max_length=15, unique=True)
    Secret_Info = models.CharField(max_length=200)

    def __str__(self):
        return self.Username

class LoginModel(models.Model):
    Username=models.CharField(max_length=30, unique=True)
    Password=models.CharField(max_length=15, unique=True)

class AdminModel(models.Model):
    Username = models.CharField(max_length=40, unique=True)
    Password = models.CharField(max_length=10, unique=True)

class Category(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to="files1")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    customer = models.ForeignKey(RegisterModel, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Cancelled", "Order Cancelled"),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=300)
    shipping_address = models.CharField(max_length=300)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=300, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order: " + str(self.id)
