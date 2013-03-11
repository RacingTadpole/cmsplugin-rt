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

class MetaIconsPlugin(CMSPluginBase):
    model = MetaIconsPluginModel
    name = _("Website icons")
    module = meta_module_name
    render_template = "meta_icons_plugin.html"

    def render(self, context, instance, placeholder):
        if not instance.touch_icon:
            instance.touch_icon = instance.fav_icon
        context['instance'] = instance
        return context

plugin_pool.register_plugin(MetaIconsPlugin)


