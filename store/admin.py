from django.contrib import admin
from .models import Order,Product,Customer,Category


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)