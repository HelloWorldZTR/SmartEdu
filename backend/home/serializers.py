from rest_framework import serializers
from .models import Banner, Announcement, HotTag, HomeStats, HotTopic


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class HotTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotTag
        fields = '__all__'


class HomeStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeStats
        fields = '__all__'


class HotTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotTopic
        fields = '__all__' 