from django.db import models
from users.models import User


class Conversation(models.Model):
    """对话模型"""
    participants = models.ManyToManyField(User, related_name='conversations', verbose_name='参与者')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'conversations'
        verbose_name = '对话'
        verbose_name_plural = '对话'
        ordering = ['-updated_at']
    
    def __str__(self):
        participants_names = ', '.join([user.username for user in self.participants.all()])
        return f"对话: {participants_names}"


class ChatMessage(models.Model):
    """消息模型"""
    MESSAGE_TYPES = [
        ('text', '文本'),
        ('image', '图片'),
        ('file', '文件'),
    ]
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', verbose_name='对话')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='发送者')
    content = models.TextField(verbose_name='消息内容')
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='text', verbose_name='消息类型')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')
    
    class Meta:
        db_table = 'chat_messages'
        verbose_name = '消息'
        verbose_name_plural = '消息'
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"


class Notification(models.Model):
    """通知模型"""
    NOTIFICATION_TYPES = [
        ('system', '系统通知'),
        ('competition', '比赛通知'),
        ('project', '项目通知'),
        ('application', '申请通知'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name='用户')
    title = models.CharField(max_length=200, verbose_name='通知标题')
    content = models.TextField(verbose_name='通知内容')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='system', verbose_name='通知类型')
    is_read = models.BooleanField(default=False, verbose_name='是否已读')
    is_important = models.BooleanField(default=False, verbose_name='是否重要')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'notifications'
        verbose_name = '通知'
        verbose_name_plural = '通知'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}: {self.title}"
