from .models import Project
from blog.models import Tag
from django.db.models import Q


def search_projects(request):

    keyword = ""
    if request.GET.get('search'):
        keyword = request.GET.get("search")

    tags = Tag.objects.filter(name__icontains=keyword)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=keyword) |
        Q(description__icontains=keyword) |
        Q(profile__name__icontains=keyword) |
        Q(tags__in=tags)
    )

    return projects, keyword
