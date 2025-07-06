from django.contrib import admin
from .models import Project, Job, Application, ProjectFavorite


class JobInline(admin.TabularInline):
    model = Job
    extra = 1
    fields = ('title', 'description', 'required_skills', 'headcount', 'salary_min', 'salary_max', 'salary_currency')


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0
    readonly_fields = ('applicant', 'job', 'resume', 'note', 'status', 'created_at')
    can_delete = False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'category', 'target_audience', 'status', 'created_at')
    list_filter = ('status', 'target_audience', 'category', 'created_at')
    search_fields = ('title', 'description', 'creator__username', 'tags')
    ordering = ('-created_at',)
    list_editable = ('status',)
    
    fieldsets = (
        ('基本信息', {'fields': ('title', 'description', 'creator', 'category')}),
        ('项目设置', {'fields': ('target_audience', 'tags', 'status')}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    inlines = [JobInline, ApplicationInline]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'headcount', 'salary_min', 'salary_max', 'salary_currency')
    list_filter = ('salary_currency', 'project__status')
    search_fields = ('title', 'description', 'project__title', 'required_skills')
    ordering = ('-project__created_at',)
    
    fieldsets = (
        ('基本信息', {'fields': ('project', 'title', 'description')}),
        ('要求', {'fields': ('required_skills', 'headcount')}),
        ('薪资', {'fields': ('salary_min', 'salary_max', 'salary_currency')}),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'project', 'job', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'project__status')
    search_fields = ('applicant__username', 'project__title', 'job__title')
    ordering = ('-created_at',)
    list_editable = ('status',)
    
    fieldsets = (
        ('申请信息', {'fields': ('applicant', 'project', 'job', 'resume')}),
        ('申请内容', {'fields': ('note', 'status')}),
        ('时间信息', {'fields': ('created_at', 'updated_at')}),
    )
    
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ProjectFavorite)
class ProjectFavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'project__title')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('收藏信息', {'fields': ('user', 'project')}),
        ('时间信息', {'fields': ('created_at',)}),
    )
    
    readonly_fields = ('created_at',)
