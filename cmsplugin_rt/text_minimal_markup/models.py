# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models

class TextMinimalMarkupPluginModel(CMSPlugin):
    title = models.CharField(max_length=120, blank=True, help_text=_("Optional heading"))
    promo_text = models.TextField(_("Text"), blank=True, help_text=_("Websites and email addresses will become linkable. HTML symbol codes are allowed, e.g. &amp;copy; for &copy;"))

    def __unicode__(self):
        return self.title

