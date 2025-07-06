from django.db import models


class Category(models.Model):
    """分类模型"""
    CATEGORY_TYPES = [
        ('competitions', '比赛'),
        ('projects', '项目'),
        ('shares', '分享'),
    ]
    
    name = models.CharField(max_length=50, verbose_name='分类名称')
    type = models.CharField(max_length=20, choices=CATEGORY_TYPES, verbose_name='分类类型')
    order = models.IntegerField(default=0, verbose_name='排序')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'categories'
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['order', 'id']
        unique_together = ['name', 'type']
    
    def __str__(self):
        return f"{self.get_type_display()}-{self.name}"
