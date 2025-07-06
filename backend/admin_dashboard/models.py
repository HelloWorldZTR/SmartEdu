from django.db import models
from users.models import User
from projects.models import Project


class Report(models.Model):
    """举报模型"""
    REPORT_TYPES = [
        ('project', '项目举报'),
        ('share', '分享举报'),
        ('user', '用户举报'),
        ('competition', '比赛举报'),
    ]
    
    STATUS_CHOICES = [
        ('pending', '待处理'),
        ('approved', '已处理'),
        ('rejected', '已驳回'),
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports', verbose_name='举报者')
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES, verbose_name='举报类型')
    target_id = models.IntegerField(verbose_name='目标ID')
    reason = models.TextField(verbose_name='举报原因')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    admin_note = models.TextField(blank=True, verbose_name='管理员备注')
    handled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='handled_reports', verbose_name='处理人')
    handled_at = models.DateTimeField(null=True, blank=True, verbose_name='处理时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='举报时间')
    
    class Meta:
        db_table = 'reports'
        verbose_name = '举报'
        verbose_name_plural = '举报'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.reporter.username}举报{self.get_report_type_display()}"


class AdminStats(models.Model):
    """管理员统计模型"""
    STATS_TYPES = [
        ('users', '用户统计'),
        ('projects', '项目统计'),
        ('competitions', '比赛统计'),
        ('shares', '分享统计'),
    ]
    
    stats_type = models.CharField(max_length=20, choices=STATS_TYPES, verbose_name='统计类型')
    data = models.JSONField(verbose_name='统计数据')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'admin_stats'
        verbose_name = '管理员统计'
        verbose_name_plural = '管理员统计'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_stats_type_display()} - {self.created_at.strftime('%Y-%m-%d')}"
