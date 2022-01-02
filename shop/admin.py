from django.contrib import admin
from .models import Category, Product


class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class prodadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'img']
    list_editable = ['price', 'stock', 'img']
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Category, catadmin)
admin.site.register(Product, prodadmin)
