from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Conversation, ChatMessage, Notification
from .serializers import ConversationSerializer, MessageSerializer, NotificationSerializer


# Create your views here.


class ConversationListView(generics.ListAPIView):
    """获取聊天列表"""
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)


class ConversationDetailView(generics.RetrieveAPIView):
    """获取聊天记录"""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        conversation_id = self.kwargs['conversation_id']
        return ChatMessage.objects.filter(conversation_id=conversation_id)


class SendMessageView(APIView):
    """发送消息"""
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationListView(generics.ListAPIView):
    """获取系统通知"""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class NotificationReadView(APIView):
    """标记通知为已读"""
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, notification_id):
        try:
            notification = Notification.objects.get(
                id=notification_id,
                user=request.user
            )
            notification.is_read = True
            notification.save()
            return Response({'message': '标记成功'})
        except Notification.DoesNotExist:
            return Response({'error': '通知不存在'}, status=status.HTTP_404_NOT_FOUND)
