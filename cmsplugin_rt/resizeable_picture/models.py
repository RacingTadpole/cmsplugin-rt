# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models

class ResizeablePicturePluginModel(CMSPlugin):
    """
    A Resizeable Picture with or without a link
    """
    CENTER = "center"
    LEFT = "left"
    RIGHT = "right"
    FLOAT_CHOICES = ((CENTER, _("center")),
                     (LEFT, _("left")),
                     (RIGHT, _("right")),
                     )

    image = models.ImageField(_("image"), upload_to=CMSPlugin.get_media_path)
    url = models.CharField(_("link"), max_length=255, blank=True, null=True, help_text=_("if present image will be clickable"))
    page_link = models.ForeignKey(Page, verbose_name=_("page"), null=True, blank=True, help_text=_("if present image will be clickable"))
    alt = models.CharField(_("alternate text"), max_length=255, blank=True, null=True, help_text=_("textual description of the image"))
    longdesc = models.CharField(_("long description"), max_length=255, blank=True, null=True, help_text=_("additional description of the image"))
    float = models.CharField(_("side"), max_length=10, blank=True, null=True, choices=FLOAT_CHOICES)
    img_width = models.CharField(_("width"), max_length=10, blank=True, help_text=_("if present, image will be scaled to this width (in pixels), e.g. 100. Alternatively enter a percentage of the view, e.g. 100%; the picture will rescale if the window's size changes"))
    img_max_width = models.CharField(_("max width"), max_length=10, blank=True, help_text=_("if present, image will not exceed this width (in pixels), e.g. 100. More commonly, enter a percentage of the view, e.g. 100% would prevent the picture from being wider than the view."))
    img_height = models.CharField(_("height"), max_length=10, blank=True, help_text=_("if present, image will be scaled to this height (in pixels), e.g. 80."))
    img_max_height = models.CharField(_("max height"), max_length=10, blank=True, help_text=_("if present, image will not exceed this height (in pixels), e.g. 80. Or enter a percentage of the view's height."))

    def __unicode__(self):
        if self.alt:
            return self.alt[:40]
        elif self.image:
            # added if, because it raised attribute error when file wasn't defined
            try:
                return u"%s" % basename(self.image.path)
            except:
                pass
        return "<empty>"
