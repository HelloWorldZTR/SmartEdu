from django.contrib import admin
from .models import Share


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'tech_stack_preview', 'likes_count', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content', 'author__username', 'tech_stack')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('基本信息', {'fields': ('title', 'content', 'author', 'category')}),
        ('技术信息', {'fields': ('tech_stack',)}),
        ('点赞信息', {'fields': ('likes',)}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def tech_stack_preview(self, obj):
        return f"{len(obj.tech_stack)}项技术"
    tech_stack_preview.short_description = '技术栈'
    
    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = '点赞数'
