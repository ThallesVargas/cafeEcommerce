from django.contrib import admin
from .models import Product, Type
# Register your models here.

class  TypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified']
	search_fields = ['name', 'slug']
	list_filter = ['created', 'modified']

class  ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'tipo', 'created', 'modified']
	search_fields = ['name', 'slug', 'tipo__name']
	list_filter = ['created', 'modified']

admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)