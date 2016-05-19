from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    url = models.URLField()
    user = models.OneToOneField(User, unique=True)
    profile_picture = models.ImageField(upload_to=settings.MEDIA_ROOT)

class Tag(models.Model):
    name  = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', related_name="tags")

class Post(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    caption = models.TextField(max_length=2200)
    likes = models.PositiveIntegerField(default=0)
    # tags = models.ManyToManyField(Tag, related_name="posts")
    user = models.ForeignKey('UserProfile')
    date_created = models.DateTimeField(auto_now_add=True)
    #comments

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    user = models.ForeignKey('UserProfile')
    text = models.TextField(max_length=2200)
    date_created = models.DateTimeField(auto_now_add=True)
