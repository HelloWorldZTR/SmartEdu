from django.urls import path
from . import views

urlpatterns = [
    path('admin/reports', views.ReportListView.as_view(), name='report-list'),
    path('admin/reports/<int:pk>', views.ReportDetailView.as_view(), name='report-detail'),
    path('admin/stats', views.AdminStatsView.as_view(), name='admin-stats'),
] 