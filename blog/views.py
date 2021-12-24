from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Category
from .forms import ArticleForm

# Create your views here.
def index(request):

    articles = Article.objects.filter(state=1)
    categories = Category.objects.filter(state=1)
    return render(
        request, "blog/index.html", {"articles": articles, "categories": categories}
    )


def show(request, slug):

    # try:
    #     article = Article.objects.get(slug=slug)
    # except:
    #     raise Http404()

    article = get_object_or_404(Article, slug=slug)

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
