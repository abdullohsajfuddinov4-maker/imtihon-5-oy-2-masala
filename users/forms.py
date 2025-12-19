from django import forms
from .models import CustomUser

class CustomUserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','image','address',]

    def clean(self):
        data = super().clean()
        if data.get('password1') != data.get('password2') :
            raise forms.ValidationError('password mas emas')
        return date


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','image','address',]



class CustomUserChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(label='password',widget=forms.PasswordInput)
    new_password = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    def clean(self):
        date = super().clean()
        if self.data['new_password'] != self.data['confirm_new_password']:
            raise forms.ValidationError('Yangi prollar mas emas')
        return date

    def save(self, commit = True):
        user = super().save(commit=False)
        if user.check_password(self.cleaned_data['old_password']):
             raise forms.ValidationError('Eski parol hato')
        user.set_password(self.cleaned_data['new_password'])
        user.save()
        return user
