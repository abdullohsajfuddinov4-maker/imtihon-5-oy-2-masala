from django.contrib import admin
from .models import Product, Category,Comments

admin.site.register(Comments)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'make',
        'category',
        'price',
        'size',
        'country',
    )

    list_filter = (
        'category',
        'make',
        'country',
    )

    search_fields = (
        'name',
        'make',
        'country',
    )

    ordering = ('-id',)
