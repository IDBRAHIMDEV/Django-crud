from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField


LIST_STATE = ((0, "disable"), (1, "enable"))

# Create your models here.
class Article(models.Model):

    state = IntegerField(default=0, choices=LIST_STATE)
    title = CharField(max_length=120, blank=True, null=True, unique=True)
    description = TextField(null=True)
    category = ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField("Tag")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):

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
