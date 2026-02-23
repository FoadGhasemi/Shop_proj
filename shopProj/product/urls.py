from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('details/<slug:slug>', views.product_details, name= 'details'),
    path('search/', views.product_search, name= 'search'),
    path('comment/<int:pk>/', views.product_comment, name='comment'),
]
