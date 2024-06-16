# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from skills.models import Skill
from projects.models import Project

 
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Project
        fields = ('title', 'description',"type","role","skills","imagePath","projectUrl","imageUrl")

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Skill
        fields = ('name', 'description',"classification","icon")