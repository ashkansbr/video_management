from django.urls import path, include
from .views import CategoryView, VideoApi

urlpatterns = [
    path('videos/', VideoApi.as_view(), name='video-list'),
    path('categories/', CategoryView.as_view(), name='category'),
]