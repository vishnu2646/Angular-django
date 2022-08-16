from dataclasses import fields
from urllib import request
from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('teamId','teamName')


class EmployeeSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()
    # team = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('employeeId','employeeName', 'dateofJoined', 'address', 'phone', 'team', 'image_url')
        
    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri( obj.image.url)
