from django.shortcuts import render
from management.forms import *
from api.models import UserProfile
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        userForm = UserCreationForm(data=request.POST)
        userProfileForm = UserProfileCreationForm(request.POST, request.FILES)

        print userForm.is_valid()
        print userProfileForm.is_valid()
        if (userForm.is_valid() and userProfileForm.is_valid()):
            user = userForm.save()
            userProfile = userProfileForm.save(commit=False)
            userProfile.user = user
            userProfile.url = 'http://' + request.get_host() + '/user/' + user.username + '/'
            userProfile.save()

            messages.success(request, "Sucessfully registered!")

            user = authenticate(username=user.username, password=userForm.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.info(request, userForm.errors)
            messages.info(request, userProfileForm.errors)

    # request.method == GET
    # else:
    #     userForm = UserCreationForm()
    #     userProfileForm = UserProfileCreationForm()

    return render(request, 'registration/register.html')
