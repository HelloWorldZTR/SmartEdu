from django.contrib import admin
from .models import Report, AdminStats


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'report_type', 'target_id', 'status', 'created_at')
    list_filter = ('report_type', 'status', 'created_at')
    search_fields = ('reporter__username', 'reason')
    ordering = ('-created_at',)
    list_editable = ('status',)
    
    fieldsets = (
        ('举报信息', {'fields': ('reporter', 'report_type', 'target_id', 'reason')}),
        ('处理状态', {'fields': ('status', 'admin_note', 'handled_by', 'handled_at')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)


@admin.register(AdminStats)
class AdminStatsAdmin(admin.ModelAdmin):
    list_display = ('stats_type', 'data_preview', 'created_at')
    list_filter = ('stats_type', 'created_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('统计信息', {'fields': ('stats_type', 'data')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)
    
    def data_preview(self, obj):
        return f"{len(obj.data)}项数据"
    data_preview.short_description = '数据预览'
