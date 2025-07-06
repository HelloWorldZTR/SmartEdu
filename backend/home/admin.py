from django.contrib import admin
from .models import Banner, Announcement, HotTag, HomeStats, HotTopic


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('order',)
    list_editable = ('order', 'is_active')
    
    fieldsets = (
        ('基本信息', {'fields': ('title', 'image', 'link')}),
        ('显示设置', {'fields': ('order', 'is_active')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'announcement_type', 'is_important', 'is_active', 'created_at')
    list_filter = ('announcement_type', 'is_important', 'is_active', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    list_editable = ('is_important', 'is_active')
    
    fieldsets = (
        ('公告信息', {'fields': ('title', 'content', 'announcement_type')}),
        ('显示设置', {'fields': ('is_important', 'is_active')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)


@admin.register(HotTag)
class HotTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)
    ordering = ('-count',)
    list_editable = ('count', 'is_active')
    
    fieldsets = (
        ('标签信息', {'fields': ('name', 'count')}),
        ('显示设置', {'fields': ('is_active',)}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)


@admin.register(HomeStats)
class HomeStatsAdmin(admin.ModelAdmin):
    list_display = ('total_users', 'total_projects', 'total_competitions', 'total_shares', 'updated_at')
    ordering = ('-updated_at',)
    
    fieldsets = (
        ('统计数据', {'fields': ('total_users', 'total_projects', 'total_competitions', 'total_shares')}),
        ('时间信息', {'fields': ('updated_at',)}),
    )
    
    readonly_fields = ('updated_at',)


@admin.register(HotTopic)
class HotTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'count', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'tag')
    ordering = ('-count', '-created_at')
    list_editable = ('count', 'is_active')
    
    fieldsets = (
        ('话题信息', {'fields': ('title', 'tag', 'count')}),
        ('显示设置', {'fields': ('is_active',)}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)
