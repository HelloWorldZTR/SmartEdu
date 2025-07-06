from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Banner, Announcement, HotTag, HomeStats, HotTopic
from .serializers import (
    BannerSerializer, AnnouncementSerializer, HotTagSerializer,
    HomeStatsSerializer, HotTopicSerializer
)
from users.models import User
from projects.models import Project
from competitions.models import Competition
from shares.models import Share
from projects.serializers import ProjectSerializer
from competitions.serializers import CompetitionSerializer
from shares.serializers import ShareSerializer


class BannerListView(generics.ListAPIView):
    """获取轮播图"""
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
    permission_classes = [permissions.AllowAny]


class HomeCompetitionListView(generics.ListAPIView):
    """获取首页比赛列表"""
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 10))
        category = self.request.query_params.get('category')
        queryset = Competition.objects.filter(is_active=True)
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset[:limit]


class HomeProjectListView(generics.ListAPIView):
    """获取首页项目列表"""
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 10))
        status = self.request.query_params.get('status')
        queryset = Project.objects.all()
        if status:
            queryset = queryset.filter(status=status)
        return queryset[:limit]


class HomeShareListView(generics.ListAPIView):
    """获取首页分享列表"""
    serializer_class = ShareSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 20))
        category = self.request.query_params.get('category')
        queryset = Share.objects.all()
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset[:limit]


class AnnouncementListView(generics.ListAPIView):
    """获取首页公告列表"""
    queryset = Announcement.objects.filter(is_active=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        limit = int(self.request.query_params.get('limit', 5))
        announcement_type = self.request.query_params.get('type')
        queryset = Announcement.objects.filter(is_active=True)
        if announcement_type:
            queryset = queryset.filter(announcement_type=announcement_type)
        return queryset[:limit]


class HotTagListView(generics.ListAPIView):
    """获取热门标签"""
    queryset = HotTag.objects.filter(is_active=True)
    serializer_class = HotTagSerializer
    permission_classes = [permissions.AllowAny]


class HotTopicListView(generics.ListAPIView):
    """获取热门话题"""
    queryset = HotTopic.objects.filter(is_active=True)
    serializer_class = HotTopicSerializer
    permission_classes = [permissions.AllowAny]


class HomeStatsView(APIView):
    """获取首页统计数据"""
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        stats = {
            'totalUsers': User.objects.count(),
            'totalProjects': Project.objects.count(),
            'totalCompetitions': Competition.objects.filter(is_active=True).count(),
            'totalShares': Share.objects.count(),
            'hotTopics': HotTopic.objects.filter(is_active=True)[:5].values('id', 'title', 'tag', 'count')
        }
        return Response(stats)
