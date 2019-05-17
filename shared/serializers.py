from rest_framework import serializers

from .models import Company, Activity, Work


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'short_name', 'long_name', 'type', 'address')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id', 'title', 'icon', 'order', 'description')
