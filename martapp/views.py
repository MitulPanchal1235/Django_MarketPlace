from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from rest_framework.renderers import JSONRenderer
from .serializers import *
import json
from .filters import *
# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        data=Posts.objects.all()
        mf=Datafilter(request.GET,data)
        data=mf.qs
        return render(request,'home.html',{'data':data,'mf':mf})
    else:
        if request.method== 'POST':
            username= request.POST.get('username1')
            password=request.POST.get('password11')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                data=Posts.objects.all()
                mf=Datafilter(request.GET,data)
                data=mf.qs
                return render(request,'home.html',{'data':data,'mf':mf})
            else:
                messages.info(request,'username or password is in correct')
    return render(request,'loginpage.htm')                
def logoutuser(request):
    logout(request)
    return redirect('loginpage')
def register(request):
    if request.user.is_authenticated:
        data=Posts.objects.all()
        mf=Datafilter(request.GET,data)
        data=mf.qs
        return render(request,'home.html',{'data':data,'mf':mf})
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            if pass1 == pass2:
                newuser=User.objects.create_user(username=username,email=email,password=pass1)
                newuser.save()
                Profile.objects.create(user=newuser,)
                return redirect('loginpage')
            else:
                messages.info(request,'password or confirm-password mismatch!!!')    
                return redirect('loginpage') 
def forgot(request):
    return render(request,'forgot.html')
@login_required(login_url='loginpage')
def home(request):
    data=Posts.objects.all()
    mf=Datafilter(request.GET,data)
    data=mf.qs
    return render(request,'home.html',{'data':data,'mf':mf})
@login_required(login_url='loginpage')    
def profile(request):
    data=Profile.objects.get(user=request.user)
    postdata=Posts.objects.filter(user=request.user).order_by('-dop')
    proform=Profileform(instance=data)
    if request.method == "POST":
        proform=Profileform(request.POST,request.FILES,instance=data)
        if proform.is_valid():
            proform.save()
            data=Posts.objects.all()
            mf=Datafilter(request.GET,data)
            data=mf.qs
            return render(request,'home.html',{'data':data,'mf':mf})
    context={'proform':proform,'data':data,'postdata':postdata}
    return render(request,'profile.html',context)
@login_required(login_url='loginpage') 
def post(request):
    form=Postform(initial={'user':request.user})
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES,initial={'user':request.user})
        if form.is_valid():
            form.save()
            data=Posts.objects.all()
            mf=Datafilter(request.GET,data)
            data=mf.qs
            return render(request,'home.html',{'data':data,'mf':mf})
    context={'form':form}
    return render(request,'post.html',context)    
@login_required(login_url='loginpage')    
def view(request,pk):
    data=Posts.objects.get(id=pk)
    prof=Profile.objects.get(user=data.user)
    context={'data':data,'profile':prof}
    return render(request,'view.html',context)
@login_required(login_url='loginpage') 
def update(request,pk):
    data=Posts.objects.get(id=pk)
    form=Postform(instance=data)
    if request.method=='POST':
        form=Postform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            data=Posts.objects.all()
            mf=Datafilter(request.GET,data)
            data=mf.qs
            return render(request,'home.html',{'data':data,'mf':mf})
    context={'form':form,'data':data}
    return render(request,'update.html',context)
@login_required(login_url='loginpage')
def deletepost(request,pk):
    data=Posts.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('profile')
    context={'form':data}
    return render(request,'deletepsot.html',context)
def videofile(request,pk):
    data=Posts.objects.get(id=pk)
    d1={'url':str(data.video)}
    json_data=json.dumps(d1)
    return HttpResponse(json_data,"application/json")