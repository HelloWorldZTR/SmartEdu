from rest_framework import generics, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Project, Job, Application, ProjectFavorite
from .serializers import ProjectSerializer, ProjectCreateSerializer, JobSerializer, ApplicationSerializer, ProjectFavoriteSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    """项目列表和创建"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'target_audience', 'status']
    search_fields = ['title', 'description', 'tags']
    ordering_fields = ['created_at', 'updated_at']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """项目详情、更新、删除"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProjectMemberView(APIView):
    """
    获取项目成员（申请列表），包含申请id、申请人名字、申请岗位、申请状态、申请描述
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, project_id):
        applications = Application.objects.filter(project_id=project_id)
        data = []
        for app in applications:
            data.append({
                "id": app.id,
                "applicant_name": app.applicant.username if app.applicant else "",
                "applicant_id": app.applicant.id if app.applicant else "",
                "job_id": app.job.id if app.job else "",
                "job_title": app.job.title if app.job else "",
                "status": app.status,
                "note": app.note,
            })
        return Response(data)


class JobApplyView(APIView):
    """申请岗位"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, project_id, job_id):
        try:
            project = Project.objects.get(id=project_id)
            job = Job.objects.get(id=job_id, project=project)
            
            # 检查是否已经申请过
            if Application.objects.filter(project=project, job=job, applicant=request.user).exists():
                return Response({'error': '您已经申请过这个岗位'}, status=status.HTTP_400_BAD_REQUEST)
            
            application = Application.objects.create(
                project=project,
                job=job,
                applicant=request.user,
                resume=request.user.resume,
                note=request.data.get('note', '')
            )
            
            serializer = ApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Project.DoesNotExist, Job.DoesNotExist):
            return Response({'error': '项目或岗位不存在'}, status=status.HTTP_404_NOT_FOUND)


class ProjectApplicationsView(generics.ListAPIView):
    """获取项目申请列表"""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Application.objects.filter(project_id=project_id)


class ApplicationHandleView(APIView):
    """处理申请"""
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, project_id, application_id):
        try:
            application = Application.objects.get(
                id=application_id,
                project_id=project_id,
                project__creator=request.user
            )
            
            action = request.data.get('action')
            if action == 'accept':
                application.status = 'accepted'
            elif action == 'reject':
                application.status = 'rejected'
            else:
                return Response({'error': '无效的操作'}, status=status.HTTP_400_BAD_REQUEST)
            
            application.save()
            serializer = ApplicationSerializer(application)
            return Response(serializer.data)
        except Application.DoesNotExist:
            return Response({'error': '申请不存在'}, status=status.HTTP_404_NOT_FOUND)


class ProjectFavoriteView(APIView):
    """收藏/取消收藏项目"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
            favorite, created = ProjectFavorite.objects.get_or_create(
                user=request.user,
                project=project
            )
            if created:
                return Response({'message': '收藏成功'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': '已经收藏过了'}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({'error': '项目不存在'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, project_id):
        try:
            favorite = ProjectFavorite.objects.get(
                user=request.user,
                project_id=project_id
            )
            favorite.delete()
            return Response({'message': '取消收藏成功'}, status=status.HTTP_200_OK)
        except ProjectFavorite.DoesNotExist:
            return Response({'error': '未收藏该项目'}, status=status.HTTP_404_NOT_FOUND)


class FavoriteProjectsView(generics.ListAPIView):
    """获取收藏的项目列表"""
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Project.objects.filter(favorited_by__user=self.request.user)


class ProjectSearchView(generics.ListAPIView):
    """搜索项目"""
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Project.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tags__contains=[query])
            )
        return Project.objects.none()


class MyCreatedProjectsView(generics.ListAPIView):
    """获取我创建的项目"""
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Project.objects.filter(creator=self.request.user)
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset.order_by('-created_at')


class MyParticipatedProjectsView(generics.ListAPIView):
    """获取我参与的项目"""
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # 获取用户申请并被接受的项目的岗位
        accepted_applications = Application.objects.filter(
            applicant=self.request.user,
            status='accepted'
        )
        project_ids = accepted_applications.values_list('project_id', flat=True).distinct()
        
        queryset = Project.objects.filter(id__in=project_ids)
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset.order_by('-created_at')


class MyApplicationsView(generics.ListAPIView):
    """获取我的申请记录"""
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Application.objects.filter(applicant=self.request.user)
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset.order_by('-created_at')
