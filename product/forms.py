from django import forms
from .models import Product ,Comments

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','name','make','price','size','country','desc','image',]

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Nomi juda qisqa (min. 3 harf)")
        return name

    def clean_size(self):
        size = self.cleaned_data['size']
        if size <= 18:
            raise forms.ValidationError("razmer juda kichik")
        return size


class CommentsForm(forms.ModelForm):
    rate = forms.IntegerField(min_value=0,max_value=5,required=False)
    class Meta:
        model = Comments
        fields = ['text','rate','image_comment']
