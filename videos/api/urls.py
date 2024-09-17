from django.urls import path, include
from .views import CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='category'),
]