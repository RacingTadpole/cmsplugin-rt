# Plugin models

from cms.models.pluginmodel import CMSPlugin
from cms.models.pagemodel import Page
from django.utils.translation import ugettext_lazy as _
from django.db import models

class ButtonPluginModel(CMSPlugin):
    CLASS_CHOICES =(("", _("default")),
                    ("btn-primary", _("primary")),
                    ("btn-info", _("info")),
                    ("btn-success", _("success")),
                    ("btn-warning", _("warning")),
                    ("btn-danger", _("danger")),
                    ("btn-inverse", _("inverse")),
                    ("btn-link", _("link")),
    )
    SIZE_CHOICES = (("", _("default")),
                    ("btn-large", _("large")),
                    ("btn-small", _("small")),
                    ("btn-mini", _("mini")),
                    )
    button_type = models.CharField(_("button type"), max_length=16, blank=True, choices=CLASS_CHOICES)
    button_size = models.CharField(_("button size"), max_length=16, blank=True, choices=SIZE_CHOICES)
    button_link = models.CharField(max_length=80, default='', blank=True)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), blank=True, null=True, help_text=_("A link to a page overrides the above button link."))
    button_text = models.CharField(max_length=80, default='here', help_text=_("HTML symbol codes are allowed, e.g. &amp;hearts; for &hearts;."))
    arrows = models.BooleanField()
    
    def __unicode__(self):
        return self.button_text

    search_fields = ('button_text','button_link',)

