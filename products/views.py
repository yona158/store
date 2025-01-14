from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request,'products/product.html')


def products(request):
    pro=Product.objects.all()
    # x={'pro': pro.order_by('-price')}
    # x={'pro': str(pro.count())}
    # x={'pro': pro.exclude(category='phone')}
    return render(request, 'products/products.html', {'pro':pro})
    # return render(request, 'products/products.html', {'pro': Product.objects.get(name='oil')})

    # return render(request,'products/products.html',{'pro':[Product.objects.get(price=100)]})
    # return render(request,'products/products.html',{'pro':Product.objects.all()})