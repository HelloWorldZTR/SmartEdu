from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'is_active', 'order', 'created_at')
    list_filter = ('type', 'is_active', 'created_at')
    search_fields = ('name',)
    ordering = ('order', 'name')
    list_editable = ('is_active', 'order')
    
    fieldsets = (
        ('基本信息', {'fields': ('name', 'type')}),
        ('显示设置', {'fields': ('is_active', 'order')}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
