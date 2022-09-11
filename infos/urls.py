from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from .views import main_page, about_me_page, contact_page


urlpatterns = [
    path('', main_page),
    path('me/', about_me_page),
    path('contact/', contact_page),
]