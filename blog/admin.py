from django.contrib import admin
from .models import Image, Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body', 'publish', 'updated', 'status']

@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']