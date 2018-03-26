from django.contrib import admin

# Register your models here.

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'price', 'image_name', 'description', 'date_created', 'date_updated')  
    list_editable = ('title', 'price', 'author', 'image_name', 'description')
    list_filter = ('title', 'author')
    search_fields = ['title', 'author', 'description']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(Book, BookAdmin)

