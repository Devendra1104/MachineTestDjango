from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    project_name = models.CharField(max_length=150,)
    created_by = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

class Client(models.Model):
    client_name = models.CharField(max_length=150)
    projects = models.ManyToManyField(Project,related_name='project')
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.client_name

