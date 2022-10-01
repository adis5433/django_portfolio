from django.urls import path
from .views import posts_list, single_post, authors_list, single_author, edit_single_post

app_name="posts"
urlpatterns = [
    path('posts/', posts_list, name="post_list"),
    path('posts/<id>/', single_post, name="post"),
    path('authors/', authors_list, name="author_list"),
    path('authors/<id>/', single_author, name="author"),
    path('edit_post/<post_id>/', edit_single_post, name="edit-post"),
]