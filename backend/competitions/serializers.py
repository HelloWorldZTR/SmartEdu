from rest_framework import serializers
from .models import Competition
from categories.serializers import CategorySerializer


class CompetitionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Competition
        fields = '__all__' 