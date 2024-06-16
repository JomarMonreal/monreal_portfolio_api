# import viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

 
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
    permission_classes = [IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Skill.objects.all()
 
    # specify serializer to be used
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]