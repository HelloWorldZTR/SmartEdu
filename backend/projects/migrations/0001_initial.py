# Generated by Django 5.2.4 on 2025-07-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, verbose_name='申请说明')),
                ('status', models.CharField(choices=[('pending', '待处理'), ('accepted', '已接受'), ('rejected', '已拒绝')], default='pending', max_length=20, verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='申请时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '申请',
                'verbose_name_plural': '申请',
                'db_table': 'applications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='岗位标题')),
                ('description', models.TextField(verbose_name='岗位描述')),
                ('required_skills', models.JSONField(default=list, verbose_name='所需技能')),
                ('headcount', models.IntegerField(default=1, verbose_name='招聘人数')),
                ('salary_min', models.IntegerField(blank=True, null=True, verbose_name='最低薪资')),
                ('salary_max', models.IntegerField(blank=True, null=True, verbose_name='最高薪资')),
                ('salary_currency', models.CharField(default='CNY', max_length=10, verbose_name='薪资货币')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '岗位',
                'verbose_name_plural': '岗位',
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='项目标题')),
                ('description', models.TextField(verbose_name='项目描述')),
                ('target_audience', models.CharField(choices=[('school', '校级'), ('department', '院级'), ('national', '国家级')], default='school', max_length=20, verbose_name='目标受众')),
                ('tags', models.JSONField(blank=True, default=list, verbose_name='标签')),
                ('status', models.CharField(choices=[('recruiting', '招募中'), ('in_progress', '进行中'), ('completed', '已完成'), ('cancelled', '已取消')], default='recruiting', max_length=20, verbose_name='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'projects',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProjectFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name': '项目收藏',
                'verbose_name_plural': '项目收藏',
                'db_table': 'project_favorites',
            },
        ),
    ]
