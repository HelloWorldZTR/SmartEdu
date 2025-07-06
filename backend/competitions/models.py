from django.db import models
from users.models import User
from categories.models import Category


class Competition(models.Model):
    """比赛模型"""
    title = models.CharField(max_length=200, verbose_name='比赛标题')
    description = models.TextField(verbose_name='比赛描述')
    organizer = models.CharField(max_length=100, verbose_name='主办方')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    deadline = models.DateField(verbose_name='截止日期')
    tags = models.JSONField(default=list, blank=True, verbose_name='标签')
    poster = models.ImageField(upload_to='competitions/', blank=True, null=True, verbose_name='海报')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'competitions'
        verbose_name = '比赛'
        verbose_name_plural = '比赛'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
