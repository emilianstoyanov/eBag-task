from django.contrib import admin

from category_tree.models import Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'parent']

