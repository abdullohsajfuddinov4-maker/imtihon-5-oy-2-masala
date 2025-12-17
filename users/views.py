from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserRegisterForm


class RegisterView(View):
    def get(self, request):
        form = CustomUserRegisterForm()
        return render(request, 'user/regis.html', {'form': form})

    def post(self, request):
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
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
