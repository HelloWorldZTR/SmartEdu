from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """自定义用户模型"""
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    points = models.IntegerField(default=0)
    skills = models.JSONField(default=list, blank=True)
    interests = models.JSONField(default=list, blank=True)
    
    # 使用email作为用户名
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '用户'
    
    def __str__(self):
        return self.username


class Resume(models.Model):
    """用户简历模型"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    education = models.JSONField(default=list, blank=True)
    skills = models.JSONField(default=list, blank=True)
    projects = models.JSONField(default=list, blank=True)
    self_evaluation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'resumes'
        verbose_name = '简历'
        verbose_name_plural = '简历'
    
    def __str__(self):
        return f"{self.user.username}的简历"


class UserStats(models.Model):
    """用户统计信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='stats')
    total_projects = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    total_applications = models.IntegerField(default=0)
    accepted_applications = models.IntegerField(default=0)
    total_shares = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user_stats'
        verbose_name = '用户统计'
        verbose_name_plural = '用户统计'
    
    def __str__(self):
        return f"{self.user.username}的统计信息"
