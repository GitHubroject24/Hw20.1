from typing import Tuple

from django.contrib import admin
from catalog.models import Product, Category
from blog.models import Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description", "category",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "photo", "is_published")
    list_filter = ("title",)
    search_fields = ("title", "body",)


