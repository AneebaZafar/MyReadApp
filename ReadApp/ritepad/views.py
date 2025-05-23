from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return redirect('read/')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        try:
            validate_password(pass1)
        except ValidationError as e:
            return HttpResponse('<br>'.join(e.messages))  # Display validation errors

        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        
    return render (request,'ritepad/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/read')
            
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'ritepad/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

