from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    # get the cart
    cart = Cart(request)

    # get_prods with out (request)!!!!!!
    cart_products = cart.get_prods
    quantities = cart.get_quants

    return render(request, 'cart/cart_summary.html', {"cart_products":cart_products, 'quantities':quantities})

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        
        # get the stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        # save to   session
        cart.add(product=product, quantity=product_qty)

        # get cart quantity
        cart_quantity = cart.__len__()

        # return response
        # return JsonResponse({'Product Name: ': product.name})
        return JsonResponse({'qty: ': cart_quantity})



def cart_delete(request):
    pass

def cart_update(request):
    pass

