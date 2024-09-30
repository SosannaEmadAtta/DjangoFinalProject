

from users.models import Users
from django.db.models import Q, Max, Min
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import Cart,CartItem
from product.models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

# Create your views here.
# @csrf_protect
# def create_product(request):
#     context={}
#     # product=Product.objects.all()
#     if request.method == 'POST':
#         name=request.POST['name']
#         price= request.POST['price']
#         # description=request.POST['description']
#         # image=request.POST['image']
# 
#         product=Product(name=name,price=price)
#         # product.session.create()
#         product.save()
#         context['prod']=product
#         return render(request,'cart/details.html',context)
#     return render(request,'cart/create_product.html',context)
# 
# def list_products(request):
#     context = {}
#     product = Product.objects.all()
#     context['prod'] = product
#     return render(request, 'cart/listing_product.html', context)

@login_required(login_url='/login')
def add_to_cart(request,product_id):
    if 'cart' not in request.session:
        request.session['cart']={}
    cart=request.session['cart']

    product_id_str = str(product_id)
    if str(product_id_str) in cart:
        cart[product_id_str]['quantity']+=1
    else:
        cart[product_id_str]={'quantity':1}

    request.session['cart'] =cart

    product = Product.objects.get(id=product_id)
    cart_obj, created = Cart.objects.get_or_create(user=request.user, is_paid=False)
    cart_item=CartItem.objects.filter(product_id=product_id,cart_id=cart_obj ).first()
    if cart_item:
        cart_item.quantity+=1
        cart_item.save()
        print('added')
    else:

        quantity = cart[product_id_str]['quantity']
        CartItem.objects.create(product_id=product,quantity=quantity,cart_id=cart_obj)
        print('created')
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):
    # session_cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    cart_obj = Cart.objects.filter(user=request.user).first()
    if cart_obj:
        for cart_item in CartItem.objects.filter(cart_id=cart_obj):
            cart_items.append({
                'product_id': cart_item.product_id.id,
                'product_name': cart_item.product_id.name,
                'quantity': cart_item.quantity,
                'price_total': cart_item.product_id.price * cart_item.quantity,
            })
            total_price += cart_item.product_id.price * cart_item.quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required(login_url='/login')
def inc_quantity(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_obj = Cart.objects.get(user=request.user, is_paid=False)
    cart_item=CartItem.objects.filter(product_id=product,cart_id=cart_obj).get()
    if cart_item:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('cart:cart_detail')


@login_required(login_url='/login')
def dec_quantity(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_obj = Cart.objects.get(user=request.user, is_paid=False)
    cart_item=CartItem.objects.filter(product_id=product,cart_id=cart_obj).get()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart:cart_detail')
