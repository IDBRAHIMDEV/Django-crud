from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):

    articles = Article.objects.filter(state=1)
    return render(request, "blog/index.html", {"articles": articles})


def show(request, id):

    article = Article.objects.get(pk=id)
    return render(request, "blog/show.html", {"article": article})


def create(request):

    form = ArticleForm

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

    return render(request, "blog/create.html", {"form": form})


def edit(request, id):

    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

    return render(request, "blog/edit.html", {"form": form})
