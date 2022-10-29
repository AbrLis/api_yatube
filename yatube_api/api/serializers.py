from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ("id", "text", "pub_date", "author", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ("id", "text", "author", "post", "created")
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "slug", "description")
        model = Group
