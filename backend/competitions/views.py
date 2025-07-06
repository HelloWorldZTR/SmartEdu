from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Competition
from .serializers import CompetitionSerializer


class CompetitionListView(generics.ListCreateAPIView):
    """比赛列表和创建"""
    queryset = Competition.objects.filter(is_active=True)
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'organizer']
    search_fields = ['title', 'description', 'tags']
    ordering_fields = ['deadline', 'created_at']


class CompetitionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """比赛详情、更新、删除"""
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
