from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Share
from .serializers import ShareSerializer, ShareCreateSerializer


class ShareListView(generics.ListCreateAPIView):
    """分享列表和创建"""
    queryset = Share.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content', 'tech_stack']
    ordering_fields = ['created_at', 'likes']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ShareCreateSerializer
        return ShareSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ShareDetailView(generics.RetrieveUpdateDestroyAPIView):
    """分享详情、更新、删除"""
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

class HotShareListView(generics.ListAPIView):
    """热门分享列表"""
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return self.queryset.order_by('-likes')[:5]