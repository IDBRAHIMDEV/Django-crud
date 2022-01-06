from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):

    projects = Project.objects.filter(state=True)
    context = {"projects": projects}
    return render(request, 'portefolio/index.html', context)
