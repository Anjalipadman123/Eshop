from django.contrib import admin
from .models import *

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

 #Register your models here.
admin.site.register (Category)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)