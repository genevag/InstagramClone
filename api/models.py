from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    url = models.URLField()
    user = models.OneToOneField(User, unique=True)
