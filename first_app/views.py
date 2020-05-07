from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Song,Album

# Create your views here.
def index(request):
    return render(request,'index.html')

def songs(request,id):
    song=Song.objects.raw('''select a.album_title,a.img,s.id,s.song_name,s.song_url,s.song_artist from first_app_album as a join first_app_song as s on a.id=s.album_id_id
where a.id=%s;
    '''%(id))
    return render(request,'songs.html',{'s':song})

def album(request,category):
    a=Album.objects.filter(category=category)
    return render(request,'album.html',{'a':a})

def play(request,song_name):
    p=Song.objects.filter(song_name=song_name)
    album_id=p.values('album_id')[0]['album_id']
    img=Album.objects.filter(id=album_id).values('img')[0]['img']
    playlist=Song.objects.filter(album_id=album_id).order_by('song_name')
    category=Album.objects.filter(id=album_id).values('category')[0]['category']
    s=Album.objects.exclude(id=album_id).filter(category=category)
    return render(request,'play.html',{'p':p,'img':img,'playlist':playlist,'s':s})



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