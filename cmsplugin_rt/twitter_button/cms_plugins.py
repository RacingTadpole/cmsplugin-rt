from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import *

class BasePlugin(CMSPluginBase):
    name = None
    module = _("Social Networking")
    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context

class TwitterButtonPlugin(BasePlugin):
    model = TwitterButtonPluginModel
    name = "Twitter 'tweet' button"
    render_template = 'twitter_button_plugin.html'
    
plugin_pool.register_plugin(TwitterButtonPlugin)
