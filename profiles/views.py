from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login',user)
    context={'form':form}
    return render(request,'register.html',context)
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get("password")
        #print(username,password)
        user=authenticate(username=username,password=password)
        if user is None:
            context={'error':'Invalid username or password'}
            return render(request,'login.html',context)
        login(request,user)
        return redirect('/') #where should the user should be redirected after loging in 
        
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'logout.html')