from ..models import Category, Video

def get_categories():
    return Category.objects.all()


def get_videos():
    return Video.objects.all()
