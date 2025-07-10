from django.urls import path
from . import views

urlpatterns = [
    # 项目基本操作
    path('projects', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    
    # 岗位申请
    path('projects/<int:project_id>/jobs/<int:job_id>/apply', views.JobApplyView.as_view(), name='job-apply'),
    
    # 项目申请管理
    path('projects/<int:project_id>/applications', views.ProjectApplicationsView.as_view(), name='project-applications'),
    path('projects/<int:project_id>/applications/<int:application_id>', views.ApplicationHandleView.as_view(), name='application-handle'),
    path('projects/<int:project_id>/members', views.ProjectMemberView.as_view(), name='project-members'),

    # 项目收藏
    path('projects/<int:project_id>/favorite', views.ProjectFavoriteView.as_view(), name='project-favorite'),
    path('projects/favorites', views.FavoriteProjectsView.as_view(), name='favorite-projects'),
    
    # 项目搜索
    path('projects/search', views.ProjectSearchView.as_view(), name='project-search'),
    
    # 我的项目相关
    path('projects/my-created', views.MyCreatedProjectsView.as_view(), name='my-created-projects'),
    path('projects/my-participated', views.MyParticipatedProjectsView.as_view(), name='my-participated-projects'),
    path('projects/my-applications', views.MyApplicationsView.as_view(), name='my-applications'),
] 