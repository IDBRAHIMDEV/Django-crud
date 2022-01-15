from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from account.models import Profile
from api.serializers import ArticleSerializer, ProjectSerializer
from blog.models import Article, Category, Tag
from portefolio.models import Project


from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def get_routes(request):

    routes = [
        {"GET": "/api/projects"},
        {"GET": "/api/projects/:id"},
        {"POST": "/api/projects"},
        {"PUT": "/api/projects/:id"},
        {"DELETE": "/api/projects/:id"},
    ]

    return Response(routes)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_projects(request):
    print(request.user.profile)
    projects = Project.objects.all()
    projectSerializer = ProjectSerializer(projects, many=True)

    return Response(projectSerializer.data)


@api_view(["GET"])
def get_project(request, id):
    project = Project.objects.get(pk=id)
    projectSerializer = ProjectSerializer(project, many=False)

    return Response(projectSerializer.data)


@api_view(["GET", "POST"])
def list_or_create_article(request):

    if request.method == "GET":
        articles = Article.objects.all()
        articleSerializer = ArticleSerializer(articles, many=True)

        return Response(articleSerializer.data)

    if request.method == "POST":

        my_data = request.data

        category = Category.objects.get(id=request.data["category"])
        tags = Tag.objects.filter(id__in=request.data["tags"])

        my_data["category"] = category.__dict__
        my_data["tags"] = [tag.__dict__ for tag in tags]

        print(my_data)

        articleSerializer = ArticleSerializer(data=my_data)

        if articleSerializer.is_valid():
            articleSerializer.save()
            return Response(articleSerializer.data, status=status.HTTP_201_CREATED)
        return Response(articleSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def one_article(request, id):

    if request.method == "GET":
        try:
            article = Article.objects.get(pk=id)
            articleSerializer = ArticleSerializer(article, many=False)
            return Response(articleSerializer.data)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        try:
            article = Article.objects.get(pk=id)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def destroy_article(request, id):
    try:
        article = Article.objects.get(pk=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
