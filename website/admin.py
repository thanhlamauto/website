from django.contrib import admin
from .models import Post, Book

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)

admin.site.register(Post, PostAdmin)
admin.site.register(Book)


