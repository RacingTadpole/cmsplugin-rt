from cms.models import CMSPlugin
from cms.models.pagemodel import Page
from django.db import models
from django.utils.translation import ugettext_lazy as _


LAYOUT_CHOICES = [
    ('standard', _('Standard')),
    ('button_count', _('Button count')),
    ('box_count', _('Box count')),
]

VERB_CHOICES = [
    ('like', _('Like')),
    ('recommend', _('Recommend')),
]

FONT_CHOICES = [
    ('arial', _('Arial')),
    ('lucida grande', _('Lucida grande')),
    ('segoe ui', _('Segoe ui')),
    ('tahoma', _('Tahoma')),
    ('trebuchet ms', _('Trebuchet ms')),
    ('verdana', _('Verdana')),
]

COLOR_CHOICES = [
    ('light', _('light')),
    ('dark', _('dark')),
]
    
class FacebookButtonPluginModel(CMSPlugin):
    layout = models.CharField(_("Layout Style"), choices=LAYOUT_CHOICES, default='standard', max_length=50)
    url = models.CharField(_("permanent URL"), default='http://', max_length=255, blank=True, help_text=_("Leave blank to use this page. Include the http:// or https:// prefix."))
    send = models.BooleanField(_("Send button"), default=True)
    show_faces = models.BooleanField(_("Show Faces"), default=True,
        help_text=_("Show profile pictures below the like button"))
    width = models.PositiveSmallIntegerField(_("Width"), default=None, null=True,
        blank=True, help_text=_("Leave empty for auto scaling"))
    verb = models.CharField(_("Verb to display"), choices=VERB_CHOICES, default='like', max_length=50)
    font = models.CharField(_("Font"), choices=FONT_CHOICES, default='verdana', max_length=50)
    color_scheme = models.CharField(_("Color Scheme"), choices=COLOR_CHOICES, default='light', max_length=50)

    def __unicode__(self):
        return "Facebook button"
