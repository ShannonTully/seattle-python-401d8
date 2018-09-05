from django.urls import path
from .views import ProductListApi, UserApi
from rest_framework.authtoken import views


urlpatterns = [
    path('product/', ProductListApi.as_view(), name='product_list_api'),
    path('user/', UserApi.as_view(), name='user-detail'),
    path('login', views.obtain_auth_token),
]
