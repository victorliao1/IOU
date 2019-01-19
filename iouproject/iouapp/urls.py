from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
