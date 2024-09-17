from django.db import models
from common.basemodel import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(BaseModel):
    category = models.ManyToManyField(Category, related_name='videos')
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
