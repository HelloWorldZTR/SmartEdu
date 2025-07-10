from rest_framework import serializers
from .models import Project, Job, Application, ProjectFavorite
from users.serializers import UserSerializer

class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title']

class JobSerializer(serializers.ModelSerializer):
    project = SimpleProjectSerializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'

class ProjectCreateSerializer(serializers.ModelSerializer):
    """用于创建项目的序列化器，处理jobs数据"""
    jobs = serializers.ListField(write_only=True, required=False)
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        jobs_data = validated_data.pop('jobs', [])
        project = Project.objects.create(**validated_data)
        
        # 创建关联的jobs
        for job_data in jobs_data:
            # 处理salary字段
            salary = job_data.pop('salary', {})
            if salary:
                job_data['salary_min'] = salary.get('min')
                job_data['salary_max'] = salary.get('max')
                job_data['salary_currency'] = salary.get('currency', 'CNY')
            
            # 处理requiredSkills字段
            if 'requiredSkills' in job_data:
                job_data['required_skills'] = job_data.pop('requiredSkills')
            
            Job.objects.create(project=project, **job_data)
        
        return project


class ProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    jobs = JobSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'


class ProjectFavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = ProjectFavorite
        fields = '__all__' 