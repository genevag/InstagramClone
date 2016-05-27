from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from api.serializers import *
import cloudinary

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

        result = cloudinary.uploader.upload(request.POST.get('image'))
        image_url = result["url"]

        # post = Post.objects.create(image=request.POST.get('image'), caption=request.POST.get('caption'), user=userprofile)
        post = Post.objects.create(image=image_url, caption=request.POST.get('caption'), user=userprofile)
        post.parseTags()
        post.save()
        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        posts = Post.objects.all()
        for post in posts:
            post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

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


# def getImage(request):
#     return Response(200)

class PostLikes(generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        likes = post.getLikes()
        return Response({'likes': likes}, status=status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        userprofile = UserProfile.objects.get(user=request.user)

        try:
            post.like(userprofile)
            post.save()
        except Exception as e:
            return Response({"message": e.message}, status=status.HTTP_409_CONFLICT)

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        userprofile = UserProfile.objects.get(user=request.user)

        try:
            post.unlike(userprofile)
            post.save()
        except Exception as e:
            return Response({"message": e.message}, status=status.HTTP_409_CONFLICT)

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostComments(generics.GenericAPIView):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        comments = post.comments.order_by('-date_created')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_pk, format=None):
        try:
            post = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            return Response({"message": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        userprofile = UserProfile.objects.get(user=request.user)

        comment = Comment.objects.create(text=request.POST.get('text'), post=post, user=userprofile)
        comment.save()
        serializer = CommentSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
