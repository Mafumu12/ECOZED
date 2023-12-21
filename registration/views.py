from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print("Username:", username)
        print("Password:", password)
        user = authenticate(request, username = username ,password=password)
        print("Authenticated User:", user)
        if user is  not None:
            login(request,user)
            return redirect('storeapp:store')
        else:
            messages.error(request,'Invalid username or password')

            return render(request,'login.html')
    
    else:
        return render(request,'login.html',{'user': request.user})
    

def signup(request):
  

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'signup.html')
        
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'signup.html',context)

def user_logout(request):
    logout(request)  

    return redirect('storeapp:store')  

