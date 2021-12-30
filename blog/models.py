from django.db import models
from django.utils.text import slugify
from django.db.models.fields import (
    CharField,
    DateTimeField,
    IntegerField,
    SlugField,
    TextField,
)
from django.urls import reverse

from django.db.models.fields.related import ForeignKey, ManyToManyField


LIST_STATE = ((0, "disable"), (1, "enable"))

# Create your models here.
class Article(models.Model):

    state = IntegerField(default=0, choices=LIST_STATE)
    title = CharField(max_length=120, blank=True, null=True, unique=True)
    slug = SlugField(max_length=120, unique=True, db_index=True, null=True, blank=True)
    description = TextField(null=True)
    category = ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField("Tag")
    picture = models.ImageField(null=True, upload_to="articles/")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("show_article", kwargs={"slug": self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = "Categorie"

    name = CharField(max_length=20)
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = CharField(max_length=20)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
