# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns (admin view)
    search_fields = ('title', 'author')  # Search bar
    list_filter = ('publication_year', 'author')  # Filter sidebar

admin.site.register(Book, BookAdmin)