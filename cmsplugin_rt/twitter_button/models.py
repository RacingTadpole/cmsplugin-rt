from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TwitterButtonPluginModel(CMSPlugin):
    tweet_text = models.CharField(_("Tweet text"), default=None, blank=True, max_length=60, help_text=_("Leave blank to use page title"))
    hash_tag = models.CharField(_("Hash tag"), default=None, blank=True, max_length=60, help_text=_("Leave blank for none"))
    large_button = models.BooleanField(_("Large button"), default=False)

    def __unicode__(self):
        return "'Tweet' button"
