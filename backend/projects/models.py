from django.db import models
from users.models import User
from categories.models import Category


class Project(models.Model):
    """项目模型"""
    STATUS_CHOICES = [
        ('recruiting', '招募中'),
        ('in_progress', '进行中'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
    ]
    
    TARGET_AUDIENCE_CHOICES = [
        ('school', '校级'),
        ('department', '院级'),
        ('national', '国家级'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='项目标题')
    description = models.TextField(verbose_name='项目描述')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects', verbose_name='创建者')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    target_audience = models.CharField(max_length=20, choices=TARGET_AUDIENCE_CHOICES, default='school', verbose_name='目标受众')
    tags = models.JSONField(default=list, blank=True, verbose_name='标签')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='recruiting', verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'projects'
        verbose_name = '项目'
        verbose_name_plural = '项目'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Job(models.Model):
    """岗位模型"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='jobs', verbose_name='项目')
    title = models.CharField(max_length=100, verbose_name='岗位标题')
    description = models.TextField(verbose_name='岗位描述')
    required_skills = models.JSONField(default=list, verbose_name='所需技能')
    headcount = models.IntegerField(default=1, verbose_name='招聘人数')
    salary_min = models.IntegerField(null=True, blank=True, verbose_name='最低薪资')
    salary_max = models.IntegerField(null=True, blank=True, verbose_name='最高薪资')
    salary_currency = models.CharField(max_length=10, default='CNY', verbose_name='薪资货币')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'jobs'
        verbose_name = '岗位'
        verbose_name_plural = '岗位'
    
    def __str__(self):
        return f"{self.project.title}-{self.title}"


class Application(models.Model):
    """申请模型"""
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('accepted', '已接受'),
        ('rejected', '已拒绝'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications', verbose_name='项目')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', verbose_name='岗位')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', verbose_name='申请人')
    resume = models.ForeignKey('users.Resume', on_delete=models.CASCADE, related_name='applications', verbose_name='简历')
    note = models.TextField(blank=True, verbose_name='申请说明')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='申请时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'applications'
        verbose_name = '申请'
        verbose_name_plural = '申请'
        ordering = ['-created_at']
        unique_together = ['project', 'job', 'applicant']
    
    def __str__(self):
        return f"{self.applicant.username}申请{self.job.title}"


class ProjectFavorite(models.Model):
    """项目收藏模型"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_projects', verbose_name='用户')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='favorited_by', verbose_name='项目')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')
    
    class Meta:
        db_table = 'project_favorites'
        verbose_name = '项目收藏'
        verbose_name_plural = '项目收藏'
        unique_together = ['user', 'project']
    
    def __str__(self):
        return f"{self.user.username}收藏{self.project.title}"
