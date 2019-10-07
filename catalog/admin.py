from django.contrib import admin
from .models import Product, Type, Producer
# Register your models here.

class  TypeAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'created', 'modified']
	search_fields = ['name', 'slug']
	list_filter = ['created', 'modified']

class  ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'tipo', 'producer', 'created', 'modified']
	search_fields = ['name', 'slug', 'tipo__name', 'procuder__name']
	list_filter = ['created', 'modified']

class  ProducerAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'region', 'created', 'modified']
	search_fields = ['name', 'slug']
	list_filter = ['created', 'modified']

admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Producer, ProducerAdmin)