from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_list, name='cart_list'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('update/', views.cart_update, name='cart_update'),
    path('delete/', views.cart_delete, name='cart_delete'),
]