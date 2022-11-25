from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import RegistrationForm


# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


def signup(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Đăng ký thành công, chào " + user + "!")
            return redirect("signin")
        messages.error(
            request, "Đăng ký không thành công, thông tin không hợp lệ.")
    context = {'form': form}
    return render(request, "signup.html", context)


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Bạn đã đăng nhập với người dùng {username}.")
                return redirect("index")
            else:
                messages.error(request, "Username hoặc mật khẩu không hợp lệ.")
        else:
            messages.error(request, "Username hoặc mật khẩu không hợp lệ.")
    form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"form": form})


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def settings(request):
    # admin_profile = Admin.objects.get(user=request.user)

    # if request.method == 'POST':

    #     if request.FILES.get('image') == None:
    #         image = admin_profile.profileimg
    #         bio = request.POST['bio']
    #         location = request.POST['location']

    #         admin_profile.profileimg = image
    #         admin_profile.bio = bio
    #         admin_profile.location = location
    #         admin_profile.save()
    #     if request.FILES.get('image') != None:
    #         image = request.FILES.get('image')
    #         bio = request.POST['bio']
    #         location = request.POST['location']

    #         admin_profile.profileimg = image
    #         admin_profile.bio = bio
    #         admin_profile.location = location
    #         admin_profile.save()

    #     return redirect('settings')
    # return render(request, 'settings.html', {'admin_profile': admin_profile})
    return render(request, 'settings.html')


def nhandienbienso(request):
    return render(request, 'nhandienbienso.html')


def quanlykhachhang(request):
    return render(request, 'quanlykhachhang.html')


def quanlygiaxe(request):
    return render(request, 'quanlygiaxe.html')


def dangkyguixe(request):
    return render(request, 'dangkyguixe.html')
