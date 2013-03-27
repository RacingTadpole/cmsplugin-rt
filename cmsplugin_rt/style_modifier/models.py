# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models
from django.conf import settings

class StyleModifierPluginModel(CMSPlugin):
    """
    Adds a style element to change the css styling on the fly
    """
    GENERIC_CLASSES = (("body", _("everything")),
                     ("p", _("paragraphs")),
                     ("hr", _("horizontal lines")),
                     (".plugin_picture", _("picture plugins")),
                     (".footer", _("footer")),
                     (".footer a, .footer a:link, .footer a:visited, .footer a:hover, .footer a:active", _("footer links")),
                     )
    
    BOOTSTRAP_CLASSES = (
                     (".navbar,#navbar", _("navigation bar")),
                     (".hero-unit", _("hero")),
                     (".jumbotron", _("jumbo banner")),
                     (".container", _("containers")),
                     (".btn", _("buttons")),
                     (".btn:hover, .btn:active, .btn.focus, .btn.disabled, .btn[disabled]", _("active buttons")),
                     (".btn.btn-primary", _("primary buttons")),
                     (".btn.btn-primary:hover, .btn.btn-primary:active, .btn.btn-primary.focus", _("active primary buttons")),
                     (".dropdown-menu", _("dropdown menus")),
                     (".sidenav a", _("side navigation menu")),
                     (".sidenav .active a", _("active side nav menu")),
                     )

    JQUERY_MOBILE_CLASSES = (
                     (".ui-body-b,.ui-dialog.ui-overlay-b", _("background body")),
                     (".ui-btn-up-b", _("buttons and bars")),
                     (".ui-btn-hover-b", _("buttons and bars, hover state")),
                     )

    front_end = getattr(settings,'RT_FRONT_END_FRAMEWORK','BOOTSTRAP').upper()
    extra_classes = getattr(settings,'RT_MORE_STYLE_CLASSES',())

    if (front_end=="BOOTSTRAP"):
        CLASS_CHOICES = GENERIC_CLASSES + (("",_("---------")),) + BOOTSTRAP_CLASSES + (("",_("---------")),) + extra_classes
    elif (front_end=="JQUERY-MOBILE"):
        CLASS_CHOICES = GENERIC_CLASSES + (("",_("---------")),) + JQUERY_MOBILE_CLASSES + (("",_("---------")),) + extra_classes
    else:
        CLASS_CHOICES = GENERIC_CLASSES + (("",_("---------")),) + extra_classes

    ALIGN_CHOICES = (("left", _("left")),
                     ("center", _("centre")),
                     ("right", _("right"))
                     )

    mod_class = models.CharField(_("class to modify"), max_length=120, choices=CLASS_CHOICES)
    background_image = models.ImageField(_("background image"), upload_to=CMSPlugin.get_media_path, blank=True, help_text=_("Leave blank for none."))
    background_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name, e.g. green or darkgreen (no spaces!), or an RGB code like #f2f2f0. Leave blank for default."))
    top_gradient_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    bottom_gradient_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    font_family = models.CharField(max_length=64, blank=True, help_text=_("Leave blank for default."))
    text_color = models.CharField(max_length=32, blank=True, help_text=_("Use a simple name or RGB code. Leave blank for default."))
    text_shadow = models.CharField(max_length=32, blank=True, help_text=_("Horizontal and vertical shadow distance followed by a color, e.g. 2px 2px black. Leave blank for default."))
    text_align =  models.CharField(max_length=32, blank=True, choices=ALIGN_CHOICES, help_text=_("Leave blank for default."))
    freeform =  models.CharField(max_length=96, blank=True, help_text=_("Enter your own css if desired, e.g. padding: 5px;"))
    def __unicode__(self):
        for (x,y) in self.CLASS_CHOICES:
            if self.mod_class==x:
                return y.decode()
        return self.mod_class
