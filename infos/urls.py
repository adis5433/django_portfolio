from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .views import main_page, about_me_page, contact_page
from posts.views import posts_list, authors_list


urlpatterns = [
    path('', main_page, name = "greetings"),
    path('me/', about_me_page, name = "about_me"),
    path('contact/', contact_page, name = "contact"),
    path('posts/', posts_list, name="posts_list"),
    path('authors/', authors_list, name="authors_list"),

]