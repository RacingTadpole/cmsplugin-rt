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

class StyleModifierPlugin(CMSPluginBase):
    model = StyleModifierPluginModel
    name = _("Style Modifier")
    module = layout_module_name
    render_template = "style_modifier.html"

    def render(self, context, instance, placeholder):
    	# we display three fields without escaping, so we can use ", ' and >
    	# but we try to ensure string cannot include any tags by removing <
    	# we also remove any refs to script or expression
    	# this is not a comprehensive solution!
        instance.mod_class = instance.mod_class.replace(u'<',u'')
        instance.freeform = instance.freeform.replace(u'<',u'')
        instance.font_family = instance.font_family.replace(u'<',u'')
        instance.mod_class = instance.mod_class.replace(u'script',u'x')
        instance.freeform = instance.freeform.replace(u'script',u'x')
        instance.font_family = instance.font_family.replace(u'script',u'x')
        instance.mod_class = instance.mod_class.replace(u'expression',u'x')
        instance.freeform = instance.freeform.replace(u'expression',u'x')
        instance.font_family = instance.font_family.replace(u'expression',u'x')
        context['instance'] = instance
        return context

plugin_pool.register_plugin(StyleModifierPlugin)


