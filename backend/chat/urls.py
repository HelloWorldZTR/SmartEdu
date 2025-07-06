from django.urls import path
from . import views

urlpatterns = [
    path('messages/conversations', views.ConversationListView.as_view(), name='conversation-list'),
    path('messages/conversations/<int:conversation_id>', views.ConversationDetailView.as_view(), name='conversation-detail'),
    path('messages/send', views.SendMessageView.as_view(), name='send-message'),
    path('notifications', views.NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:notification_id>/read', views.NotificationReadView.as_view(), name='notification-read'),
] 