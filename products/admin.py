from django.contrib import admin
from .models import Product,Test
# Register your models here.
# admin.site.register(Product)
admin.site.register(Test)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','active']
    list_display_links = ['name','price']
    list_editable = ['active']
    search_fields = ['name']
    list_filter = ['price','category']
    fields=['name','price'] 

admin.site.register(Product,ProductAdmin)
admin.site.site_header="Yolan"
admin.site.site_title="Yolan"