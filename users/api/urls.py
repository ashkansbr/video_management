from django.urls import path
from .views import RegistrationApi

urlpatterns = [
    path('users/register/', RegistrationApi.as_view(), name='user-register'),
]