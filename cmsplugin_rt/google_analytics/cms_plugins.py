from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import *

bootstrap_module_name = _("Widgets")
layout_module_name = _("Layout elements")
generic_module_name = _("Generic")
meta_module_name = _("Meta elements")

class GoogleAnalyticsPlugin(CMSPluginBase):
    model = GoogleAnalyticsPluginModel
    name = "Google analytics"
    render_template = 'google_analytics_plugin.html'
    module = meta_module_name

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'name': self.name})
        return context
    
plugin_pool.register_plugin(GoogleAnalyticsPlugin)

