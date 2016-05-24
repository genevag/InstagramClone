from django.shortcuts import render
from api.models import *

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def user_profile(request, username):

    return render(request, 'under_construction.html')
