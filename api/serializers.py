from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = ('post', )


class PostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    image = serializers.ImageField(max_length=None,use_url=True)

    comments = CommentSerializer(source='getComments', read_only=True, many=True)
    class Meta:
        model = Post
        field = ('image', 'caption', 'comments')
        # exclude = ('likes', )
