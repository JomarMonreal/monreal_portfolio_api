# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from projects.models import Project

 
# Create a model serializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Project
        fields = ('title', 'description',"type","role","skills","imagePath","projectUrl","imageUrl")