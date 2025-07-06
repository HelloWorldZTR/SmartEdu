from django.db import models


class Banner(models.Model):
    """轮播图模型"""
    title = models.CharField(max_length=200, verbose_name='标题')
    image = models.ImageField(upload_to='banners/', verbose_name='图片')
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name='链接')
    order = models.IntegerField(default=0, verbose_name='排序')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'banners'
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'
        ordering = ['order', 'id']
    
    def __str__(self):
        return self.title


class Announcement(models.Model):
    """公告模型"""
    ANNOUNCEMENT_TYPES = [
        ('system', '系统公告'),
        ('competition', '比赛公告'),
        ('project', '项目公告'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    announcement_type = models.CharField(max_length=20, choices=ANNOUNCEMENT_TYPES, default='system', verbose_name='公告类型')
    is_important = models.BooleanField(default=False, verbose_name='是否重要')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'announcements'
        verbose_name = '公告'
        verbose_name_plural = '公告'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class HotTag(models.Model):
    """热门标签模型"""
    name = models.CharField(max_length=50, unique=True, verbose_name='标签名')
    count = models.IntegerField(default=0, verbose_name='使用次数')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'hot_tags'
        verbose_name = '热门标签'
        verbose_name_plural = '热门标签'
        ordering = ['-count']
    
    def __str__(self):
        return self.name


class HomeStats(models.Model):
    """首页统计模型"""
    total_users = models.IntegerField(default=0, verbose_name='总用户数')
    total_projects = models.IntegerField(default=0, verbose_name='总项目数')
    total_competitions = models.IntegerField(default=0, verbose_name='总比赛数')
    total_shares = models.IntegerField(default=0, verbose_name='总分享数')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'home_stats'
        verbose_name = '首页统计'
        verbose_name_plural = '首页统计'
    
    def __str__(self):
        return f"首页统计 - {self.updated_at.strftime('%Y-%m-%d %H:%M')}"


class HotTopic(models.Model):
    """热门话题模型"""
    title = models.CharField(max_length=200, verbose_name='话题标题')
    tag = models.CharField(max_length=50, verbose_name='标签')
    count = models.IntegerField(default=0, verbose_name='讨论次数')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        db_table = 'hot_topics'
        verbose_name = '热门话题'
        verbose_name_plural = '热门话题'
        ordering = ['-count']
    
    def __str__(self):
        return self.title
