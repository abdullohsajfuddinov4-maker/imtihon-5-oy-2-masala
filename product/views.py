from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Product, Category, Comments
from .forms import ProductForm, CommentsForm


# ===================== PRODUCTS =====================

class ProductList(View):
    def get(self, request):
        q = request.GET.get('q', '')
        products = Product.objects.all().order_by('-id')

        if q:
            products = products.filter(name__icontains=q)

        categories = Category.objects.all()

        return render(request, 'home.html', {
            'product': products,
            'categories': categories,
            'q': q
        })


class ProductDetail(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.comments.all().order_by('-id')
        form = CommentsForm()

        return render(request, 'dateil.html', {
            'product': product,
            'comments': comments,
            'form': form,
        })


class ProductCreate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'create.html', {'form': ProductForm()})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('home')

        return render(request, 'create.html', {'form': form})


class ProductUpdate(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')

        return render(request, 'update.html', {'form': form})


class ProductDelete(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'delete.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('home')


class ProductCategory(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        categories = Category.objects.all()
        products = Product.objects.filter(category=category)

        return render(request, 'category.html', {
            'categories': categories,
            'category': category,
            'products': products,
        })


# ===================== COMMENTS =====================

class CreateCommentView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CommentsForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()

        return redirect('detail', pk=pk)


class UpdateCommentView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk, user=request.user)
        form = CommentsForm(instance=comment)
        return render(request, 'update_comment.html', {'form': form})

    def post(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk, user=request.user)
        form = CommentsForm(request.POST, request.FILES, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('detail', pk=comment.product.id)

        return render(request, 'update_comment.html', {'form': form})


class DeleteCommentView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk, user=request.user)
        product_id = comment.product.id
        comment.delete()
        return redirect('detail', pk=product_id)
