from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product
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


class LogoutView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        logout(request)
        return redirect('login')


class ProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        user = request.user
        products = user.products.all().order_by('-id')
        return render(request, 'user/profile.html',{'user':user,'products':products})


class ProfileUpdateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = CustomUserUpdateForm(instance=request.user)
        return render(request, 'user/profile_update.html', {'form': form})

    def post(self, request):
        form = CustomUserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

        return render(request, 'user/profile_update.html', {'form': form})


class CustomUserChangePasswordFormView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        form = CustomUserChangePasswordForm(instance=request.user)
        return render(request, 'user/change_pass.html', {'form': form})

    def post(self, request):
        form = CustomUserChangePasswordForm(data=request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'parol yangilandi ')
            return redirect('profile')

        return render(request, 'user/change_pass.html', {'form': form})
