
from cgitb import html
from tkinter import Button
from django.contrib import admin
from django.urls import path
from app.views import home, login, signup


urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('signup/', signup),
]
