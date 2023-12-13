from django.contrib import admin
from category_tree.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'parent']
    list_filter = ['name', 'description', 'image', 'parent']
    search_fields = ['name', 'description']

