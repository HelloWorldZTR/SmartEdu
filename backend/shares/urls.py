from django.urls import path
from . import views

urlpatterns = [
    path('shares', views.ShareListView.as_view(), name='share-list'),
    path('shares/<int:pk>', views.ShareDetailView.as_view(), name='share-detail'),
    path('hot-shares', views.HotShareListView.as_view(), name='hot-share-list'),
] 