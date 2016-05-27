from django.shortcuts import render
from api.models import *
from api.serializers import *

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('date_created')
    return render(request, 'home.html', {'posts': posts})

def user_profile(request, username):

    return render(request, 'under_construction.html')


def explore_hashtag(request, hashtag):
    tag = Tag.objects.get(name=hashtag)
    serializer = PostSerializer(tag.posts, many=True)

    return render(request, 'explore_hashtag.html', { 'posts': serializer.data })
