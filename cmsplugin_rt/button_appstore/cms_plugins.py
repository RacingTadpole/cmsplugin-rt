from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from models import *

class ButtonAppstorePlugin(CMSPluginBase):
    model = ButtonAppstorePluginModel
    name = _("App Store Button")
    render_template = "button_appstore_plugin.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['link'] = instance.button_link
        return context

plugin_pool.register_plugin(ButtonAppstorePlugin)

