from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from models import *

bootstrap_module_name = _("Widgets")
layout_module_name = _("Layout elements")
generic_module_name = _("Generic")
meta_module_name = _("Meta elements")

class HBarPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("Horizontal line")
    module = layout_module_name
    render_template = "hbar_plugin.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(HBarPlugin)


