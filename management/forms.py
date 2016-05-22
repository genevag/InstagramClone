from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.models import UserProfile
from django.conf import settings

class UserProfileCreationForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField();
    profile_picture = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ("username", "email", "password1", "password2", "profile_picture")
        exclude = ("url", )

    def save(self, commit=True):
        user = super(UserCreationForm, self)
        if user.is_valid():
            user.save(commit=False)
            print "USER VALID"
        url = settings.HOST + '/user/' + self.username
        userProfile = UserProfile(user=user, url=url)
        if userProfile.is_valid():
            userProfile.save()
            print "USER PROFILE VALID"

        return user, userProfile
