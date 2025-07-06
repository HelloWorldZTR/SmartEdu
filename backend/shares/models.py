from django.db import models
from users.models import User
from categories.models import Category


class Share(models.Model):
    """分享模型"""
    title = models.CharField(max_length=200, verbose_name='分享标题')
    content = models.TextField(verbose_name='分享内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares', verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    tech_stack = models.JSONField(default=list, blank=True, verbose_name='技术栈')
    likes = models.ManyToManyField(User, related_name='liked_shares', blank=True, verbose_name='点赞用户')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'shares'
        verbose_name = '分享'
        verbose_name_plural = '分享'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
