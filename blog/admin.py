from django.contrib import admin

# Register your models here.

from .models import Author,Tag,Post

class AuthorAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","tags","date",)
    list_display=("title","date","author",)
    prepopulated_fields={"slug":("title",)}


admin.site.register(Author)

admin.site.register(Tag)

admin.site.register(Post,PostAdmin)