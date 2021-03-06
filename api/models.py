from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField
import re

# Create your models here.
class UserProfile(models.Model):
    url = models.URLField()
    user = models.OneToOneField(User, unique=True)
    profile_picture = CloudinaryField('image')

    def getUsername(self):
        return self.user.username

class Tag(models.Model):
    name  = models.CharField(max_length=50)
    posts = models.ManyToManyField('Post', related_name="tags")

class Like(models.Model):
    user = models.ForeignKey('UserProfile', related_name="likes")
    post = models.ForeignKey('Post')


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    user = models.ForeignKey('UserProfile')
    text = models.TextField(max_length=2200)
    date_created = models.DateTimeField(auto_now_add=True)

    def getUsername(self):
        return self.user.user.username


class Post(models.Model):
    image = CloudinaryField('image')
    caption = models.TextField(max_length=2200)
    likes = models.PositiveIntegerField(default=0)
    # tags = models.ManyToManyField(Tag, related_name="posts")
    user = models.ForeignKey('UserProfile')
    date_created = models.DateTimeField(auto_now_add=True)
    #comments

    def getLikes(self):
        #return Like.objects.filter(post=self).length
        return self.likes

    def getUsername(self):
        return self.user.user.username

    def like(self, userprofile):
        if (Like.objects.filter(user=userprofile, post=self).exists()):
            raise Exception("Already Liked")

        likeRelationship = Like(user=userprofile, post=self)
        likeRelationship.save()
        likeRelationship.save()
        self.likes = self.likes + 1

    def unlike(self, userprofile):
        if (not Like.objects.filter(user=userprofile, post=self).exists()):
            raise Exception("Haven't Liked Yet")

        likeRelationship = Like.objects.get(user=userprofile, post=self)
        likeRelationship.delete()
        self.likes = self.likes - 1

    def getComments(self):
        comments = Comment.objects.filter(post=self)
        return comments

    def getTags(self):
        tags = Tag.objects.filter(posts__id = self.id)
        return tags

    def userLiked(self, userprofile):
        try:
            likeRel = Like.objects.get(user=userprofile, post=self)
        except Like.DoesNotExist:
            return False
        return True

    def parseTags(self):
        results = re.findall("#(?P<ht>([a-zA-Z0-9_])+)", self.caption)

        for item in results:
            tagName = item[0]
            tag, created = Tag.objects.get_or_create(name=tagName)
            tag.posts.add(self)
            tag.save()
