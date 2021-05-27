from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=20,null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname
class Category(models.Model):
    title = models.CharField(max_length=225)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.title
class  Product(models.Model):
    title = models.CharField(max_length=225)
    slug=models.SlugField(unique=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    marked_price = models.IntegerField()
    selling_price = models.IntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=225,null=True,blank=True)
    return_policy = models.CharField(max_length=225,null=True,blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Cart:"+ str(self.id)

class  Cartproduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    rate = models.IntegerField()
    quantity= models.IntegerField()
    subtotal=models.IntegerField()
    def __str__(self):
        return "Cart:"+str(self.cart.id)+"Cartproduct:"+str(self.id)
ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("UPI", "UPI"),
    ("NETBANKING", "NETBANKING"),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.IntegerField()
    discount = models.IntegerField()
    total = models.IntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
class Productimage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    image1 = models.ImageField(upload_to = "products/images/" , blank = True)
    image2 = models.ImageField(upload_to = "products/images/" , blank = True)
    image3 = models.ImageField(upload_to = "products/images/" , blank = True)
    def __str__(self):
        return self.product.title



class Contact(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    car_id = models.IntegerField(null=True)
    customer_need = models.CharField(max_length=100,null=True)
    car_title = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=False)
    message = models.TextField(null = False)
    phone = models.CharField(max_length=20,null=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default = datetime.now)
    def __str__(self):
        return self.email
class Contactpage(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null = True)
    phone = models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.name
class SearchTerms(models.Model):

    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    search_terms = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name_plural = "Search Terms"

    def __str__(self):
        return self.search_terms
class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
