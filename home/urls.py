from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"), # home page
    path('product_details/<int:pk>', views.product_details, name="product_details"), # product details page
    path('category_products/<int:pk>', views.category_products, name="category_products"), # search products by category
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('cart', views.cart, name="cart"),
    path('decrease_item', views.decrease_item, name="decrease_item"),
    path('increase_item', views.increase_item, name="increase_item"),
    path('delete_item', views.delete_item, name="delete_item"),
]