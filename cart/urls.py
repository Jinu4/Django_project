from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_cart, name='addcart'),
    path('remove/<int:product_id>/', views.delete, name='remove'),
    path('cart_decrement/<int:product_id>/', views.min_cart, name='cart_decrement'),

]
