from django.contrib import admin
from .models import Product ,Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
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

