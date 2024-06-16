from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Skill

# Create your views here.
def skills(request):
    myskills = Skill.objects.all()
    template = loader.get_template("all_skills.html")
    context = {
        "myskills": myskills
    }
    return HttpResponse(template.render(context,request))