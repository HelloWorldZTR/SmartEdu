from django.urls import path
from . import views

urlpatterns = [
    path('competitions', views.CompetitionListView.as_view(), name='competition-list'),
    path('competitions/<int:pk>', views.CompetitionDetailView.as_view(), name='competition-detail'),
] 