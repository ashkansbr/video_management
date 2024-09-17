from ..models import Category, Video
from django.core.exceptions import ValidationError
from django.db import transaction


@transaction.atomic
def create_video(title, description, duration, video_file, category):
    video = Video.objects.create(
        title=title,
        description=description,
        duration=duration,
        video_file=video_file
    )
    video.category.set(category)
    video.save()

    return video



@transaction.atomic
def create_category(name):
    if Category.objects.filter(name=name).exists():
        raise ValidationError(f"Category with name '{name}' already exists.")

    return Category.objects.create(name=name)
