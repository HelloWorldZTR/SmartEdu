from django.contrib import admin
from .models import Conversation, ChatMessage, Notification


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0
    readonly_fields = ('sender', 'content', 'message_type', 'is_read', 'created_at')
    can_delete = False


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'participants_display', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('participants__username',)
    ordering = ('-updated_at',)
    
    fieldsets = (
        ('对话信息', {'fields': ('participants',)}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ChatMessageInline]
    
    def participants_display(self, obj):
        return ', '.join([user.username for user in obj.participants.all()])
    participants_display.short_description = '参与者'


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'content_preview', 'message_type', 'is_read', 'created_at')
    list_filter = ('message_type', 'is_read', 'created_at')
    search_fields = ('sender__username', 'content', 'conversation__participants__username')
    ordering = ('-created_at',)
    list_editable = ('is_read',)
    
    fieldsets = (
        ('消息信息', {'fields': ('conversation', 'sender', 'content', 'message_type')}),
        ('状态', {'fields': ('is_read',)}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '内容预览'


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'notification_type', 'is_read', 'is_important', 'created_at')
    list_filter = ('notification_type', 'is_read', 'is_important', 'created_at')
    search_fields = ('user__username', 'title', 'content')
    ordering = ('-created_at',)
    list_editable = ('is_read', 'is_important')
    
    fieldsets = (
        ('通知信息', {'fields': ('user', 'title', 'content', 'notification_type')}),
        ('状态', {'fields': ('is_read', 'is_important')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)
