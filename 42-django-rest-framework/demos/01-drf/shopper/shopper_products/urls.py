from django.urls import path
from .views import (
    StoreView,
    ProductDetailView,
    ProductCreateView)


urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/add', ProductCreateView.as_view(), name='product_create'),
]
