from cms.models import CMSPlugin
from cms.models.pagemodel import Page
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GoogleFontPluginModel(CMSPlugin):
    font_family_pluses = models.CharField(_("font family name"), default='Eagle+Lake', max_length=100, help_text=_("You must use plus signs instead of spaces here. Add :b or :i for bold or italics styles. Separate multiple font families with a | symbol. See https://developers.google.com/webfonts/docs/getting_started for more."))

    def __unicode__(self):
        return self.font_family_pluses
