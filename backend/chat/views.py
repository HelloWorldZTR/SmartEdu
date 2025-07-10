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
    
    def post(self, request):
        """创建或获取与指定用户的对话"""
        participant_id = request.data.get('participant_id')
        if not participant_id:
            return Response({'error': 'participant_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            from users.models import User
            participant = User.objects.get(id=participant_id)
            
            # 不能与自己创建对话
            if participant.id == request.user.id:
                return Response({'error': 'Cannot create conversation with yourself'}, status=status.HTTP_400_BAD_REQUEST)
            
            # 查找是否已存在对话
            existing_conversation = Conversation.objects.filter(
                participants=request.user
            ).filter(
                participants=participant
            ).first()
            
            if existing_conversation:
                print(f"找到现有对话: {existing_conversation.id}")
                serializer = ConversationSerializer(existing_conversation)
                return Response(serializer.data)
            
            # 创建新对话
            print(f"创建新对话，参与者: {request.user.username} 和 {participant.username}")
            conversation = Conversation.objects.create()
            conversation.participants.add(request.user, participant)
            
            # 重新获取对话以确保数据完整
            conversation.refresh_from_db()
            
            serializer = ConversationSerializer(conversation)
            print(f"新对话创建成功: {conversation.id}, 参与者数量: {conversation.participants.count()}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except User.DoesNotExist:
            print(f"用户不存在: {participant_id}")
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"创建对话时出错: {str(e)}")
            return Response({'error': 'Failed to create conversation'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ConversationDetailView(generics.ListAPIView):
    """获取聊天记录"""
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        conversation_id = self.kwargs['conversation_id']
        # 确保用户是对话的参与者
        return ChatMessage.objects.filter(
            conversation_id=conversation_id,
            conversation__participants=self.request.user
        ).order_by('created_at')


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
