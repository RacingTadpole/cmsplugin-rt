# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.db import models

class NavbarPluginModel(CMSPlugin):
    DISPLAY_CHOICES =(("", _("default")),
                    ("navbar-fixed-top", _("fixed to top")),
                    ("navbar-fixed-bottom", _("fixed to bottom")),
                    ("navbar-static-top", _("static top")),
                    )
    USER_ICON_CHOICES = (("",_("grey")),
                         ("icon-white",_("white")),
                         )
    navbar_type = models.CharField(_("navbar type"), max_length=64, blank=True, default="navbar-fixed-top", choices=DISPLAY_CHOICES)
    inverted = models.BooleanField(default=False)
    brand = models.CharField(max_length=80, default='', blank=True)
    link_to_children = models.BooleanField(default=True, 
            help_text=_("Show links to all navigable children of the home page. NOTE: You must set the home page's id to 'home' under the advanced settings. Will not work if there is a 'softroot' in your CMS."))
    icon_type = models.CharField(_("user actions icon type"), max_length=24, blank=True, choices=USER_ICON_CHOICES)
    
    def __unicode__(self):
        if self.brand:
            return self.brand
        else:
            return ""

