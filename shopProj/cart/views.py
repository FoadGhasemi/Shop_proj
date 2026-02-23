from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from product.models import Product


def cart_list(request):
    # Get the cart
    cart = Cart(request)

    # Getting the actual prods from db as a collection
    cart_prods = cart.get_products

    # So we can update the product qty dynamically (this method returns cart/dict)
    quantities = cart.get_qty

    return render(request, 'cart/purchasing.html', {'cart_prods': cart_prods,
                                                                        'quantities': quantities})

def add_to_cart(request):
    # Get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Look up product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, quantity=product_qty)

        # debug: print cart after adding
        print('cart after add: ', cart.get_cart_contents())

        # Get Cart quantity
        cart_quantity = cart.__len__()

        # return response
        response = JsonResponse({'qty': cart_quantity,
                                 'cart': cart.get_cart_contents(),
                                 'message': f'added {product.title} to cart'
                                 })
        return response


def cart_update(request):
    # Get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

    # Update the cart
    cart.update(product_id = product_id, quantity = product_qty)
    response = JsonResponse({'qty': product_qty})
    return response


def cart_delete(request):
    # Get the cart
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))

    # Update the cart
    cart.delete(product_id = product_id)
    response = JsonResponse({'prd': product_id})
    return response
