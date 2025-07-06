from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Resume, UserStats


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('个人信息', {'fields': ('first_name', 'last_name', 'email', 'school', 'department', 'bio', 'avatar', 'level', 'points')}),
        ('技能和兴趣', {'fields': ('skills', 'interests')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_preview', 'skills_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'self_evaluation')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('基本信息', {'fields': ('user', 'self_evaluation')}),
        ('教育背景', {'fields': ('education',)}),
        ('技能', {'fields': ('skills',)}),
        ('项目经验', {'fields': ('projects',)}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def education_preview(self, obj):
        return f"{len(obj.education)}项教育经历"
    education_preview.short_description = '教育经历'
    
    def skills_preview(self, obj):
        return f"{len(obj.skills)}项技能"
    skills_preview.short_description = '技能'


@admin.register(UserStats)
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_projects', 'completed_projects', 'total_applications', 'accepted_applications')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('统计信息', {'fields': ('user', 'total_projects', 'completed_projects', 'total_applications', 'accepted_applications', 'total_shares', 'total_likes')}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
