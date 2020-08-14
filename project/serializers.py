from .models import Client,Project
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields =  ['id','project_name','created_at','created_by']
        read_only_fields = ('created_at','created_by')

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['id','client_name','created_at','created_by']

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class ClientProjectSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = ['id','client_name','projects','created_at','created_by','updated_at']

class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =  ['id','project_name','created_at','created_by']






