from .models import Book
from django.contrib import admin
admin.site.register(Book)
"register", "admin.ModelAdmin"
"list_filter", "author", "publication_year"
"search_fields", "title"

# Register your models here.
