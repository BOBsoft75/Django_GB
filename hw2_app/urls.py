from django.urls import path
from . import views
from .views import ProductUpdateView

urlpatterns = [
    path('clients/', views.client_view, name='clients'),
    path('products/', views.product_view, name='products'),
    path('orders/', views.order_view, name='orders'),
    path('products/<int:pk>/edit/',
         ProductUpdateView.as_view(), name='product_edit'),

]
