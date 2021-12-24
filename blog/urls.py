from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="list_of_articles"),
    path("<slug:slug>/", views.show, name="show_article"),
    path("create/", views.create, name="create_article"),
    path("edit/<int:id>/", views.edit, name="edit_article"),
]
