from django.contrib import admin
from .models import Category, Product, Profile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
admin.site.register(Profile)
