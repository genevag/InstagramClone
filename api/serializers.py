from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile


class PostSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Post
        # exclude = ('likes', )
