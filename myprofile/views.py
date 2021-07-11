from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image,Profile,Follow,
# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.images()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'index.html', {"images":images[::1],"users":users})


def update_profile(request):
   
   
    return render(request, 'newprofile.html')

def profile(request):
    return render(request,'profile.html')
