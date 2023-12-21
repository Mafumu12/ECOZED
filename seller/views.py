from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from storeapp.models import Product
from .forms import Product_form
# Create your views here.



@login_required
def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        my_products = products.filter(seller = request.user)
        context = {'my_products':my_products}
        return render(request,'dashboard.html',context)
    else:

     return redirect('user_login')
    
@login_required
def delete_product(request,id):
   products = Product.objects.get(pk=id)
   if request.user == products.seller:
    products.delete()
    return redirect( 'seller:dashboard')
   
@login_required
def New_Item(request):
    if request.method == 'POST':
        forms = Product_form(request.POST, request.FILES)
        if forms.is_valid():
            product = forms.save(commit=False)  # Don't save to database yet
            product.seller = request.user  # Assign the current user as the seller
            product.save()  # Now save to database
            return redirect('seller:dashboard')
    else:
        forms = Product_form()
        
    context = {'forms': forms}
    return render(request, 'newitem.html', context)

@login_required
def Edit(request,id):
   products = Product.objects.get(pk=id)
 
   if request.user == products.seller:
   
    if request.method == 'POST':
      forms = Product_form(request.POST,instance=products)
      if forms.is_valid():
         forms.save()
         return redirect('seller:dashboard')
      
    else:
       forms = Product_form(instance=products)
    context = {'forms':forms}
    return render (request,'Edit.html',context)
       
         
   