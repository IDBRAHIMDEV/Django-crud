from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Article, Category
from .forms import ArticleForm

from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.contrib.auth.decorators import login_required

# Create your views here.


class ListArticleView(ListView):
    queryset = Article.objects.filter(state=1).order_by("-created")
    template_name = "blog/index.html"
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categories'] = Category.objects.filter(state=1)

        return context


class DeleteArticleView(DeleteView):
    model = Article
    success_url = "/articles"


# class ListArticleView(View):
#     def get(self, request):
#         articles = Article.objects.filter(state=1)
#         categories = Category.objects.filter(state=1)
#         return render(
#             request, "blog/index.html", {"articles": articles,
#                                          "categories": categories}
#         )


def index(request):

    articles = Article.objects.filter(state=1)
    categories = Category.objects.filter(state=1)
    return render(
        request, "blog/index.html", {"articles": articles,
                                     "categories": categories}
    )


class ShowArticleView(DetailView):
    model = Article
    template_name = "blog/show.html"


# class ShowArticleView(View):
#     def get(self, request, slug):
#         article = get_object_or_404(Article, slug=slug)
#         return render(request, "blog/show.html", {"article": article})


def show(request, slug):

    # try:
    #     article = Article.objects.get(slug=slug)
    # except:
    #     raise Http404()

    article = get_object_or_404(Article, slug=slug)

    return render(request, "blog/show.html", {"article": article})

# Class based views


class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/create.html"
    success_url = "/articles"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.state = 1
        form.save()
        return super().form_valid(form)

    # class CreateArticleView(View):

    #     def get(self, request):
    #         form = ArticleForm
    #         return render(request, "blog/create.html", {"form": form})

    #     def post(self, request):
    #         form = ArticleForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             return redirect("list_of_articles")

    #         return render(request, "blog/create.html", {"form": form})

    # function based views


@login_required(login_url="login")
def create(request):

    form = ArticleForm

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

    return render(request, "blog/create.html", {"form": form})


class EditArticleView(View):
    def get(self, request, id):
        article = Article.objects.get(pk=id)
        form = ArticleForm(instance=article)
        return render(request, "blog/edit.html", {"form": form})

    def post(self, request, id):

        article = Article.objects.get(pk=id)
        form = ArticleForm(request.POST, instance=article, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

        return render(request, "blog/edit.html", {"form": form})


def edit(request, id):

    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("list_of_articles")

    return render(request, "blog/edit.html", {"form": form})
