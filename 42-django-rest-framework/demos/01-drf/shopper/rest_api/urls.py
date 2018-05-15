from django.urls import path
from .views import ProductListApi
from rest_framework.authtoken import views


urlpatterns = [
    path('product/', ProductListApi.as_view(), name='product_list_api'),
    path('auth-token-login/', views.obtain_auth_token),
]
