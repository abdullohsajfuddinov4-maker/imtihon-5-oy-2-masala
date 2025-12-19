from django.urls import path
from django.urls import path
from .views import RegisterView, ProfileView, LoginView, LogoutView,ProfileUpdateView,CustomUserChangePasswordFormView

urlpatterns = [
    path('regis/', RegisterView.as_view(), name='regis'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/change-password/', CustomUserChangePasswordFormView.as_view(), name='change_password'),
]

