from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from api.serializers import *

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Instagram Clone API index.")

class PostList(generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, format=None):
        posts = Post.objects.all().order_by('-date_created')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        userprofile = UserProfile.objects.get(user=request.user)

        post = Post.objects.create(image=request.POST.get('image'), caption=request.POST.get('caption'), user=userprofile)
        post.save()
        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostDetail(generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.user != post.user.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
