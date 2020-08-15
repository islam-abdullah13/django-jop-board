from django.shortcuts import render , redirect
from .forms import SignupForm , EditUser , EditProfile
from django.contrib.auth import authenticate , login
from .models import Profile
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else: 
        form = SignupForm()
    return render (request ,'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile ,})


def profile_edit(request):
    profile = Profile.objects.get (user=request.user)
    if request.method == "POST":
        userform = EditUser(request.POST,instance=request.user)
        profileform = EditProfile(request.POST,request.FILES,instance=profile)
        
        if userform.is_valid and profileform.is_valid():
            userform.save()
            myprofileform = profileform.save(commit=False)
            myprofileform.user = request.user
            myprofileform.save()
            return redirect(reverse("accounts:profile"))

    else:
        userform = EditUser(instance=request.user)
        profileform = EditProfile(instance=profile)


    return render (request ,'accounts/profile_edit.html',{"userform":userform,"profileform":profileform})

