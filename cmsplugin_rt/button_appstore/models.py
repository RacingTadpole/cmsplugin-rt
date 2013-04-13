# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

class ButtonAppstorePluginModel(CMSPlugin):

    button_link = models.URLField(_("Direct link"), help_text=_("e.g. https://itunes.apple.com/us/app/aquizzical/id627435810?mt=8&uo=4"))
    
    def __unicode__(self):
        return u"Download from iTunes"

