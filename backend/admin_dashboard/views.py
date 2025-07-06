from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Report, AdminStats
from .serializers import ReportSerializer, AdminStatsSerializer
from users.models import User
from projects.models import Project, Application
from competitions.models import Competition
from shares.models import Share


class ReportListView(generics.ListAPIView):
    """获取举报列表"""
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def get_queryset(self):
        report_type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')
        queryset = Report.objects.all()
        if report_type:
            queryset = queryset.filter(report_type=report_type)
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class ReportDetailView(generics.RetrieveUpdateAPIView):
    """举报详情和处理"""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminStatsView(APIView):
    """管理员统计数据"""
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request):
        stats = {
            'totalUsers': User.objects.count(),
            'totalProjects': Project.objects.count(),
            'totalCompetitions': Competition.objects.count(),
            'totalShares': Share.objects.count(),
            'totalApplications': Application.objects.count(),
            'pendingReports': Report.objects.filter(status='pending').count(),
            'recentUsers': User.objects.order_by('-date_joined')[:10].values('id', 'username', 'email', 'date_joined'),
            'recentProjects': Project.objects.order_by('-created_at')[:10].values('id', 'title', 'creator__username', 'created_at'),
            'recentReports': Report.objects.order_by('-created_at')[:10].values('id', 'report_type', 'status', 'created_at')
        }
        return Response(stats)
