from django.urls import path
from . import views

urlpatterns = [
    path('home/banners', views.BannerListView.as_view(), name='banner-list'),
    path('home/competitions', views.HomeCompetitionListView.as_view(), name='home-competition-list'),
    path('home/projects', views.HomeProjectListView.as_view(), name='home-project-list'),
    path('home/shares', views.HomeShareListView.as_view(), name='home-share-list'),
    path('home/announcements', views.AnnouncementListView.as_view(), name='announcement-list'),
    path('tags', views.TagListView.as_view(), name='tag-list'),
    path('topics', views.TopicListView.as_view(), name='topic-list'),
    path('home/stats', views.HomeStatsView.as_view(), name='home-stats'),
] 