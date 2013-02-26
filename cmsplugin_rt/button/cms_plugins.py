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

class ButtonPlugin(CMSPluginBase):
    model = ButtonPluginModel
    name = _("Button")
    #module = bootstrap_module_name
    render_template = "button_plugin.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        if instance.page_link:
            context['link'] = instance.page_link.get_absolute_url()
        else:
            context['link'] = instance.button_link
        return context

plugin_pool.register_plugin(ButtonPlugin)

