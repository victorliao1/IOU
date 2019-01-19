from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.money_list, name='money_list'),
    path('input/', views.new_money_owed, name='new_money_owed'),
    path('signup/', views.SignUp, name='signup'),
    path('moneylist/', views.money_list, name='money_list'),
    path('deleteEntry/<int:entry_id>/', views.deleteEntry, name='deleteEntry'),
]