from rest_framework import serializers
from .models import Share
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer


class ShareSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Share
        fields = '__all__'


class ShareCreateSerializer(serializers.ModelSerializer):
    """用于创建分享的序列化器，允许设置category ID"""
    
    class Meta:
        model = Share
        fields = ['title', 'content', 'category', 'tech_stack'] 