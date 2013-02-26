# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models

class StyleModifierPluginModel(CMSPlugin):
    """
    Adds a style element to change the css styling on the fly
    """
    CLASS_CHOICES = (("body", _("everything")),
                     (".navbar", _("navigation bar")),
                     (".jumbotron", _("jumbo banner")),
                     (".hero-unit", _("hero")),
                     (".row", _("main content")),
                     (".btn", _("buttons")),
                     (".btn:hover, .btn:active, .btn.active, .btn.disabled, .btn[disabled]", _("active buttons")),
                     (".btn-primary", _("primary buttons")),
                     (".btn-primary:hover, .btn-primary:active, .btn-primary.active, .btn-primary.disabled, .btn-primary[disabled]", _("active primary buttons")),
                     ("hr", _("horizontal lines")),
                     ('.plugin_picture', _("picture plugins")),
                     (".dropdown-menu", _("dropdown menus")),
                     (".sidenav a", _("side navigation menu")),
                     (".sidenav .active a", _("active side nav menu")),
                     )
    ALIGN_CHOICES = (("left", _("left")),
                     ("center", _("centre")),
                     ("right", _("right"))
                     )

    mod_class = models.CharField(_("class to modify"), max_length=120, choices=CLASS_CHOICES)
    background_image = models.ImageField(_("background image"), upload_to=CMSPlugin.get_media_path, blank=True, help_text=_("Leave blank for none."))
    background_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name, e.g. green or darkgreen (no spaces!), or an RGB code like #f2f2f0. Leave blank for default."))
    top_gradient_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    bottom_gradient_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    text_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    text_shadow = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    text_align =  models.CharField(max_length=32, blank=True, choices=ALIGN_CHOICES, help_text=_("Leave blank for default."))
    freeform =  models.CharField(max_length=96, blank=True, help_text=_("Enter your own css if desired, e.g. padding: 5px;"))
    def __unicode__(self):
        for (x,y) in self.CLASS_CHOICES:
            if self.mod_class==x:
                return y.decode()
        return self.mod_class
