from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryListView(generics.ListCreateAPIView):
    """分类列表和创建"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'is_active']
    ordering_fields = ['order', 'name']


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """分类详情、更新、删除"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class AllTagsView(APIView):
    """获取所有标签字符串列表"""
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        from django.db.models import Q
        from backend.projects.models import Project
        # 假设项目的tags字段为list类型
        all_tags = set()
        for project in Project.objects.all():
            for tag in (project.tags or []):
                all_tags.add(tag)
        return Response(sorted(list(all_tags)))
