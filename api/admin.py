from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from api.models import *

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
