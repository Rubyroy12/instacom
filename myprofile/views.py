from django.shortcuts import render,redirect
from .forms import NewProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def update_profile(request):
   
   
    #     form = NewProfile(request.POST,request.FILES)
    #     if form.is_valid():
    #         profile = form.save()
    #         profile.editor=current_user
    #         profile.save()
    #     return redirect('home')
    # else:
    #     form = NewProfile()
    return render(request,'newprofile.html')
