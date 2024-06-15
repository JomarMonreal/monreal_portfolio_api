from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

# Create your views here.
def projects(request):
    myprojects = Project.objects.all()
    template = loader.get_template("all_projects.html")
    context = {
        "myprojects": myprojects
    }
    return HttpResponse(template.render(context,request))