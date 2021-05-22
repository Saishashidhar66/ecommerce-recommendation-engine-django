from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Customer,Category,Product,Order,Cart,Cartproduct,Productimage,Contactpage,SearchTerms,Review])
