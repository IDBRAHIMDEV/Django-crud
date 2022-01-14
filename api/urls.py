from django.urls import path
from .views import list_or_create_article, one_article, get_project, get_routes, list_projects

urlpatterns = [
    path("routes/", get_routes),
    # routes for project App
    path("projects/", list_projects),
    path("projects/<int:id>", get_project),


    # routes for blog app
    path("articles/", list_or_create_article),
    path("articles/<int:id>", one_article),
    #path("articles/<int:id>/delete/", destroy_article),
]
