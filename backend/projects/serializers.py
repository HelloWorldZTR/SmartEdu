from rest_framework import serializers
from .models import Project, Job, Application, ProjectFavorite
from users.serializers import UserSerializer


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


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