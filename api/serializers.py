from account.models import Profile
from blog.models import Article, Category, Tag
from rest_framework import serializers
from portefolio.models import Project


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "username", "email"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)
    category = CategorySerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        exclude = ["profile"]
