from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register', views.RegisterView.as_view(), name='register'),
    path('auth/logout', views.LogoutView.as_view(), name='logout'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/me', views.UserMeView.as_view(), name='user_me'),
    path('user/profile', views.UserMeView.as_view(), name='user_profile'),
    path('user/resume', views.ResumeView.as_view(), name='user_resume'),
    path('user/<int:pk>/stats', views.UserStatsView.as_view(), name='user_stats'),
    # ... 其他用户相关接口
] 