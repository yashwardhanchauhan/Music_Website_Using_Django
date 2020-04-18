from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Songs

# Create your views here.
def index(request):
    return render(request,'index.html')

def songs(request,category):
    s=Songs.objects.filter(category=category)
    # print(s)
    return render(request,'songs.html',{'s':s})

def play(request,song_name):
    p=Songs.objects.filter(song_name=song_name)
    category=p[0].category
    s=Songs.objects.exclude(song_name=song_name).filter(category=category)
    return render(request,'play.html',{'p':p,'s':s,})


def serviceworker(request):
    return render(request,'pwabuilder-sw.js',content_type="application/javascript")


#ACCOUNT
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["pwd1"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or Password")
            return redirect('/')
        
    else:
        return render(request,'ErrorPage.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"You Have Been Logout Sucessfully")
    return redirect('/')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        if User.objects.filter(username=username).exists()==False:
            if pwd1==pwd2:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd1)
                user.save()
                messages.info(request,"User Created")
                return redirect('/')
            else:
                messages.info(request,"Password not Matched")
                return redirect('/')
        else:
            messages.info(request,"User name Already taken")
            return redirect('/')
        return redirect('/')
    else:
        return render(request,'/')