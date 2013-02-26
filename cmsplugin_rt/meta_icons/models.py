# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models

class MetaIconsPluginModel(CMSPlugin):
    fav_icon = models.ImageField(_("Bookmark icon"), upload_to=CMSPlugin.get_media_path, blank=True, help_text=_("A small square icon (either 16x16 or 32x32 pixels is best). Leave blank for none."))
    touch_icon = models.ImageField(_("Apple touch icon"), upload_to=CMSPlugin.get_media_path, blank=True, help_text=_("A square icon for mobile device home pages. For retina iPad, use 144x144 pixels. Leave blank for none."))
    def __unicode__(self):
        if self.fav_icon:
            return self.fav_icon.url
        elif self.touch_icon:
            return self.touch_icon.url
        else:
            return "No icons"

