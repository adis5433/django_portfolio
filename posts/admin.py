from django.contrib import admin
from posts.models import Post, Author
# Register your models here.

# Register your models here.




class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "content", "created", "modified", "author"]
   list_filter = ["title"]
   search_fields = ["title", "author"]




class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email']


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)