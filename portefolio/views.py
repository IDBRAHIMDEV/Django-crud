from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .helpers import search_projects
# Create your views here.


def index(request):

    projects, keyword = search_projects(request)

    item_per_page = 4
    page = request.GET.get("page")
    paginator = Paginator(projects, item_per_page)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    context = {"projects": projects,
               "keyword": keyword, "paginator": paginator}
    return render(request, 'portefolio/index.html', context)
