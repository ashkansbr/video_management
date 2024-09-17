from rest_framework import serializers
from ..models import Category, Video


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class VideoSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())


    class Meta:
        model = Video
        fields = ['title', 'description', 'duration', 'video_file', 'category']

    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        video = Video.objects.create(**validated_data)
        for category_data in categories_data:
            category = Category.objects.get_or_create(**category_data)[0]
            video.category.add(category)
        return video