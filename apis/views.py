# import viewsets
from rest_framework import viewsets

 
# import local data
from .serializers import ProjectSerializer, SkillSerializer
from projects.models import Project
from skills.models import Skill
 
# create a viewset
 
 
class ProjectViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Project.objects.all()
 
    # specify serializer to be used
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Skill.objects.all()
 
    # specify serializer to be used
    serializer_class = SkillSerializer