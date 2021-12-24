from django.contrib import admin

from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "state", "category", "created")
    list_filter = ("state", "category")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)


# Register your models here.
admin.site.register([Category, Tag])
