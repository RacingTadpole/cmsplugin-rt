from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from cmsplugin_mailchimp import models
from django.utils.translation import ugettext_lazy as _

class BasePlugin(CMSPluginBase):
    name = None
    module = _("Social Networking")
    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

class MailChimpPlugin(BasePlugin):
    model = models.MailChimpPluginModel
    name = "Mailchimp form"
    render_template = 'mailchimp_form_plugin.html'
    
plugin_pool.register_plugin(MailChimpPlugin)
