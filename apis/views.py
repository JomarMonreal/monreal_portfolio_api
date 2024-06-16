# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import ProjectSerializer
from projects.models import Project
 
# create a viewset
 
 
class ProjectViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Project.objects.all()
 
    # specify serializer to be used
    serializer_class = ProjectSerializer