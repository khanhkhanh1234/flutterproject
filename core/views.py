from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from .forms import CreateStaffForm


# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


def signup(request):
    form = CreateStaffForm()

    if request.method == 'POST':
        form = CreateStaffForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Registration successful." + user)

            return redirect("signin")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    context = {'form': form}
    return render(request, "signup.html", context)


# @login_required(login_url='signin')
# def settings(request):
#     user_staff = Staff.objects.get(user=request.user)
#
#     if request.method == 'POST':
#
#         if request.FILES.get('image') == None:
#             image = user_profile.profileimg
#             bio = request.POST['bio']
#             location = request.POST['location']
#
#             user_profile.profileimg = image
#             user_profile.bio = bio
#             user_profile.location = location
#             user_profile.save()
#         if request.FILES.get('image') != None:
#             image = request.FILES.get('image')
#             bio = request.POST['bio']
#             location = request.POST['location']
#
#             user_profile.profileimg = image
#             user_profile.bio = bio
#             user_profile.location = location
#             user_profile.save()
#
#         return redirect('settings')
#     return render(request, 'setting.html', {'user_profile': user_profile})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"signin": form})


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
