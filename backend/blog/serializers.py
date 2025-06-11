from rest_framework import serializers
from .models import Post, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    author = serializers.StringRelatedField(
        read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'excerpt', 'content', 'slug',
                  'author', 'published', 'status', 'category']
        lookup_field = 'slug'
