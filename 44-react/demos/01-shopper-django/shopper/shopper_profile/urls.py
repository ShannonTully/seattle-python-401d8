from django.urls import path
from .views import profile_view, ProfileEditView


urlpatterns = [
    path('', profile_view, name='profile'),
    path('<str:username>', profile_view, name='named_profile'),
    path('settings/<str:username>', ProfileEditView.as_view(), name='settings')
]
