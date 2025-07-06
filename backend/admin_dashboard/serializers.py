from rest_framework import serializers
from .models import Report, AdminStats


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class AdminStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminStats
        fields = '__all__' 