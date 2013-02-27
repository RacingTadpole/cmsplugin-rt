from cms.models import CMSPlugin
from cms.models.pagemodel import Page
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GoogleAnalyticsPluginModel(CMSPlugin):
    account_code = models.CharField(_("Account code"), default='UA-xxxxxxxx-x', max_length=50)
    domain_name = models.CharField(_("Domain name"), default='example.com', max_length=60)
    subdomains = models.BooleanField(_("Track subdomains"), default=False)

    def __unicode__(self):
        return self.account_code
