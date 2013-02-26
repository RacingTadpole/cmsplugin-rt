from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

class MailChimpPluginModel(CMSPlugin):
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
    title = models.CharField(max_length=120, blank=True, default="Subscribe to our mailing list")
    form_action = models.URLField(help_text=_("Please paste this in from the 'action=' part of the embedded code provided by mailchimp.com, e.g. http://yourname.us6.list-manage.com/subscribe/post?u=c73da2d768ef08412d44553ac&amp;amp;id=65df681376"))
    subscribe_text = models.CharField(max_length=60, default="Subscribe")
    button_type = models.CharField(_("button type"), max_length=16, blank=True, choices=CLASS_CHOICES)
    button_size = models.CharField(_("button size"), max_length=16, blank=True, choices=SIZE_CHOICES)

    def __unicode__(self):
        return self.title
