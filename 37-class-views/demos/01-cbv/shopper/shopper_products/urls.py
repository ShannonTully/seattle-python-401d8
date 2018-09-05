from django.urls import path
from .views import StoreView, product_detail_view, ProductCreateView


urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('products/<int:pk>', product_detail_view, name='product_detail'),
    path('products/add', ProductCreateView.as_view(), name='product_create'),
]
