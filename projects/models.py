from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    skills = models.JSONField()
    imagePath = models.CharField(max_length=255)
    projectUrl = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=255)