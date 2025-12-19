from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat.errors import messages

from .forms import CustomUserRegisterForm ,CustomUserUpdateForm,CustomUserChangePasswordForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserRegisterForm()
        return render(request, 'user/regis.html', {'form': form})

    def post(self, request):
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data.get('password1')
            user.set_password(password)

            user.save()
            login(request, user)
            return redirect('home')

        return render(request, 'user/regis.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'user/login.html', {
            'error': 'Username or password is incorrect'
        })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class ProfileView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'user/profile.html')


class ProfileUpdateView(View):
    def get(self,request):
        form = CustomUserUpdateForm(instance=request.user)
        return render(request,'user/profile_uodate.html',{'form':form})

    def post(self,request):
        form = CustomUserUpdateForm(request.POST , request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            redirect('profile',pk=user.pk)
        return render(request,'user/profile_uodate.html',{'form':form})


