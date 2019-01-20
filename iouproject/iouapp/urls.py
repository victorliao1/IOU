from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('input/', views.new_money_owed, name='new_money_owed'),
    path('signup/', views.SignUp, name='signup'),
    path('moneylist/', views.money_list, name='money_list'),
    path('deleteEntry/<int:entry_id>/', views.deleteEntry, name='deleteEntry'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    # path('payment_process', views.payment_process, name='payment_process' ),
    path('payment_done', views.payment_done, name='payment_done'),
    path('payment_canceled', views.payment_canceled, name='payment_canceled'),
]