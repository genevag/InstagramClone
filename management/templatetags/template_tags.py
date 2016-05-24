from django import template

register = template.Library()

@register.assignment_tag
def call_post_userLiked(post, userprofile):
    return post.userLiked(userprofile)
