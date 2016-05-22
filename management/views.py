from django.shortcuts import render
from management.forms import UserProfileCreationForm

# Create your views here.
def register(request):
    form = UserProfileCreationForm()

    if request.method == "POST":
        print "POST"
        print form

        form.save()
    return render(request, 'registration/register.html', { 'form': form })
