from django.shortcuts import render,redirect
# from .forms import NewProfile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def update_profile(request):
   
    # current_user = request.user
    # if request.method == 'POST':
    #     form =NewProfile(request.POST, request.FILES)
    #     if form.is_valid():
    #         article = form.save(commit=False)
    #         article.editor = current_user
    #         article.save()
    #     return redirect('home')

    # else:
    #     form =NewProfile()
    return render(request, 'newprofile.html')

def profile(request):
    return render(request,'profile.html')
