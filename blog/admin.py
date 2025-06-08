from django.contrib import admin
from .models import Author, Category, Post

admin.site.register(Author)
admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "created_at")
    search_fields = ("title",)
    list_filter = ("category", "author")
