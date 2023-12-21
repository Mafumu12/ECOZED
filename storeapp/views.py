from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.http import JsonResponse
import json
from .forms import Shipping_Info_form
# Create your views here.

 

def store(request):
    cart = None  # Initialize cart variable
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            # Create a new Customer instance associated with the user
            customer = Customer.objects.create(user=request.user, name=request.user.username)

        cart, created = Cart.objects.get_or_create(customer=customer, completed=False)
        cartitems = cart.cartitems_set.all()

    items = request.GET.get('items', '')
    products = Product.objects.all()
    categories = request.GET.get('categories', '')

    if items:
        products = products.filter(Q(Name__icontains=items) | Q(Description__icontains=items))

    if categories:
        products = products.filter(category__name__icontains=categories)

    products = products.order_by('-Created')[:6]  # Apply slicing after filtering

    context = {'products': products, 'items': items, 'categories': categories, 'cart': cart}
    return render(request, 'store.html', context)


def detail(request, id):
    cart = None  # Initialize cart variable
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            # Create a new Customer instance associated with the user
            customer = Customer.objects.create(user=request.user, name=request.user.username)

        cart, created = Cart.objects.get_or_create(customer=customer, completed=False)
        cartitems = cart.cartitems_set.all() 






    products = Product.objects.get(pk=id)
    related_products = Product.objects.filter(category=products.category).exclude(pk=id)[:3]
    context = {'products': products, 'related_products': related_products, 'cart':cart}
    return render(request, 'detail.html', context)


def cart(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            # Create a new Customer instance associated with the user
            customer = Customer.objects.create(user=request.user, name=request.user.username)

        cart, created = Cart.objects.get_or_create(customer=customer, completed=False)
        cartitems = cart.cartitems_set.all()
        context = {'cartitems': cartitems, 'cart':cart}
    else:
        try:
             cart = json.loads(request.COOKIES['cart'])
        except:
             cart = {}
        print('cart:',cart)
        cartitems = []
        context = {"get_cart_total":0,"items_total":0}

    return render(request, 'cart.html', context)



def checkout(request):
    cart = None  # Initialize cart variable
    
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            # Create a new Customer instance associated with the user
            customer = Customer.objects.create(user=request.user, name=request.user.username)

        cart, created = Cart.objects.get_or_create(customer=customer, completed=False)
        cartitems = cart.cartitems_set.all() 

    if request.method=='POST':
        form = Shipping_Info_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout')
    
    else:
        form = Shipping_Info_form()
    context = {'form':form,'cart':cart,'cartitems':cartitems}

    return render(request,'checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer, completed=False)

    cartitem, _ = Cartitems.objects.get_or_create(cart=cart, product=product)

    if action == 'add':
        cartitem.quantity += 1
    elif action == 'remove':
        cartitem.quantity -= 1
        if cartitem.quantity <= 0:
            cartitem.delete()
    cartitem.save()

    return JsonResponse('item was added', safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProduct = data['qfp']
    product = Cartitems.objects.filter(product__Name=quantityFieldProduct).last()
    product.quantity = quantityFieldValue  # Corrected this line
    product.save()
    return JsonResponse("Quantity updated", safe=False)