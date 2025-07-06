from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Resume, UserStats

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'avatar', 'school', 'department', 'bio',
            'level', 'points', 'skills', 'interests', 'date_joined'
        ]

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class UserStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStats
        fields = '__all__' 