from django.contrib import admin
from .models import Author, Book
from rest_framework.authtoken.admin import TokenAdmin


# Register your models here.
admin.site.register(Author)
admin.site.register(Book)



TokenAdmin.raw_id_fields = ('user',)
