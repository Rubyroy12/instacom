from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image,Profile,Follow
# Create your views here.
# def home(request):
#     return render(request, 'home.html')



def index(request):
    images = Image.images()
    users = User.objects.exclude(id=request.user.id)
    return render(request,'index.html', {"images":images[::1],"users":users})
