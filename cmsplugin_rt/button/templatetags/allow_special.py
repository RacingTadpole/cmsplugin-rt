from django import template

register = template.Library()

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

@register.filter(needs_autoescape=True)
def allow_special(text, autoescape=None):
    """This filter turns any http(s)://www.*  or www.* into a link,
       and any mailto:x@example.com into a clickable email field x@example.com.
       It also allows any &xxxxx; code through to be rendered in html
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    
    addr = r'[A-Za-z0-9\/\.\-]+\.[A-Za-z0-9\/\.\-]+[A-Za-z0-9]'
    mailaddr = r'[A-Za-z0-9\._]+@[A-Za-z0-9\._]+[A-Za-z0-9]'
    phttp = re.compile(r'(?P<links>https?://'+addr+')')
    pwww = re.compile(r'(?P<links>www\.'+addr+')')
    #pmail = re.compile(r'mailto:(?P<mail>[A-Za-z0-9\._@]+[A-Za-z0-9])')
    pmail = re.compile(r'(?P<mail>'+mailaddr+')')
    special = r'&#?[0-9a-z]{0,8};'
    pspecial = re.compile(special)
    #p = re.compile(r'(https?://www\.'+addr+'|www\.'+addr+'|mailto:[A-Za-z0-9\._@]+[A-Za-z0-9]|'+special+')')
    p = re.compile(r'(https?://'+addr+'|www\.'+addr+'|'+mailaddr+'|'+special+')')
    result = ""
    for field in p.split(text):
        if phttp.match(field):
            result += "<a href='%s' target='_blank'>%s</a>" % (field, field)
        elif pwww.match(field):
            result += "<a href='http://%s' target='_blank'>%s</a>" % (field, field)
        elif pmail.match(field):
            result += "<a href='mailto:%s'>%s</a>" % (field, field)
        elif pspecial.match(field):
            result += field
        else:
            result += esc(field)
    
    return mark_safe(result)

