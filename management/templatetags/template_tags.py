from django import template
from django.utils.safestring import mark_safe
import re
register = template.Library()

@register.assignment_tag
def call_post_userLiked(post, userprofile):
    return post.userLiked(userprofile)


# Modified from : https://gist.github.com/timmyomahony/1023144 2016-05-26
@register.simple_tag(name='parseHashtagMentions')
def parseHashtagMentions(text, hostname):
	""" Replace @ and #'s with links to twitter"""
	return mark_safe(
		re.sub(r"#(?P<ht>([a-zA-Z0-9_])+)", r"<a href='http://" + hostname + "/explore/tags/\g<ht>' target='_blank'>#\g<ht></a>",
		re.sub(r"@(?P<un>([a-zA-Z0-9_]){1,15})", r"<a href='/user/\g<un>' target='_blank'>@\g<un></a>", text))
		)
parseHashtagMentions.mark_safe=True
