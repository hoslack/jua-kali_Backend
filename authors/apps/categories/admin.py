from django.contrib import admin
from .models import Category


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, AuthorAdmin)
