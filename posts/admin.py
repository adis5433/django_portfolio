from django.contrib import admin
from posts.models import Post, Author, Tag
# Register your models here.

# Register your models here.




class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "content", "created", "modified", "author"]
   list_filter = ["title"]
   search_fields = ["title", "author"]




class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)