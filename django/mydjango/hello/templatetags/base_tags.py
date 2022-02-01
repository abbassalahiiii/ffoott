from django import template
from..models import category

register=template.Library()

@register.simple_tag

def title():
    return "MYSITE"

@register.inclusion_tag("myhtml/partial/category_navbar.html")
def category_navbar():
    return {
        "cat":category.objects.filter(status=True)
    }

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content):
    return{
        "request":request,
        "link_name":link_name,
        "link":"account:{}".format(link_name),
        "content":content,

    }