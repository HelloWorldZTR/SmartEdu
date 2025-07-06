from django.contrib import admin
from .models import Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'category', 'deadline', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'deadline', 'created_at')
    search_fields = ('title', 'description', 'organizer', 'tags')
    ordering = ('-created_at',)
    list_editable = ('is_active',)
    
    fieldsets = (
        ('基本信息', {'fields': ('title', 'description', 'organizer', 'category')}),
        ('比赛设置', {'fields': ('deadline', 'tags', 'is_active')}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
