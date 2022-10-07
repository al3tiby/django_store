from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Author)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Product)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20



@admin.register(models.Slider)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
