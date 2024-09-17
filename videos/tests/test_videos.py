import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from videos.models import Video, Category
from rest_framework import status
from datetime import timedelta
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def video_category():
    return Category.objects.create(name="Test Category")

@pytest.mark.django_db
def test_create_video(api_client, video_category):

    url = reverse('video-list')

    video_file = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")

    data = {
        "title": "Test Video",
        "description": "A test video.",
        "duration": timedelta(minutes=10),
        "video_file": video_file,
        "category": [video_category.id]
    }


    response = api_client.post(url, data, format='multipart')


    assert response.status_code == status.HTTP_201_CREATED
