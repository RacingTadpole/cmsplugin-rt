# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from os.path import basename
from django.db import models

class OpenGraphPluginModel(CMSPlugin):
    og_title = models.CharField(_("title"), max_length=255, help_text=_("Page title"))
    og_type = models.CharField(_("type"), max_length=60, default="website", help_text=_("Only certain types, e.g. 'website', are allowed.  See http://developers.facebook.com/docs/opengraphprotocol/#types for more info."))
    og_url = models.CharField(_("permanent URL"), default="http://", max_length=255, help_text=_("Include the http:// or https://."))
    og_image = models.ImageField(_("icon"), upload_to=CMSPlugin.get_media_path, help_text=_("A square icon (over 200x200 pixels is recommended)."))
    fb_app_id = models.CharField(_("Facebook app ID"), max_length=80, blank=True, help_text=_("Required for Facebook."))
    og_site_name = models.CharField(_("site name"), max_length=255, blank=True, help_text=_("Optional name for your site."))
    og_description = models.CharField(_("description"), max_length=255, blank=True, help_text=_("Optional one to two sentence description of your page."))
    def __unicode__(self):
        return self.og_title

