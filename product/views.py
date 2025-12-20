from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Product , Category
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProductList(View):
    def get(self,request):
        product = Product.objects.all().order_by('-id')
        categories = Category.objects.all()
        context = {'product': product, 'categories': categories}
        return render(request,'home.html',context)



class ProductDetail(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        context = {'product':product}
        return render(request,'dateil.html',context)


class ProductCreate(View):
    def get(self,request):
        form = ProductForm()
        context = {'form':form}
        return render(request,'create.html',context)

    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('home')
        return render(request, 'create.html', context={'form':form})


class ProductUpdate(View):
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        form = ProductForm(instance=product)

        context = {'form':form}
        return render(request,'update.html',context)

    def post(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'create.html', context={'form':form})


class ProductDelete(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, 'delete.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('home')


class ProductCategory(View):
    def get(self, request, pk):
        categories = Category.objects.all()
        category = get_object_or_404(Category, pk=pk)
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {
            'categories': categories,
            'category': category,
            'products': products,
        })




class ProductList(View):
    def get(self, request):
        q = request.GET.get('q', '')

        product = Product.objects.all().order_by('-id')

        if q:
            product = product.filter(name__icontains=q)

        categories = Category.objects.all()

        context = {
            'product': product,
            'categories': categories,
            'q': q
        }
        return render(request, 'home.html', context)