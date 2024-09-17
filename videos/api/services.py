from ..models import Category
from django.core.exceptions import ValidationError
from django.db import transaction


@transaction.atomic
def create_category(name):
    if Category.objects.filter(name=name).exists():
        raise ValidationError(f"Category with name '{name}' already exists.")

    return Category.objects.create(name=name)
