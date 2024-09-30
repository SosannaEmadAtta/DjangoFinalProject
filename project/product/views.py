from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
# Create your views here.
@csrf_protect
def create_product(request):
    context={}
    # product=Product.objects.all()
    if request.method == 'POST':
        name=request.POST['name']
        price= request.POST['price']
        description=request.POST['description']
        image=request.POST['image']

        product=Product(name=name,price=price,description=description,image=image)
        # product.session.create()
        product.save()
        context['prod']=product
        return render(request,'product/details.html',context)
    return render(request,'product/create_product.html',context)

def list_products(request):
    context = {}
    product = Product.objects.all()
    context['prod'] = product
    return render(request, 'product/listing_product.html', context)



