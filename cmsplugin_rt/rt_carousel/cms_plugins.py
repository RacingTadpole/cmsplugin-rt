from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from models import RTCarouselPluginModel

bootstrap_module_name = _("Widgets")
layout_module_name = _("Layout elements")
generic_module_name = _("Generic")
meta_module_name = _("Meta elements")

class RTCarouselPlugin(CMSPluginBase):
    model = RTCarouselPluginModel
    name = _("Carousel")
    module = bootstrap_module_name
    render_template = "rt_carousel_plugin.html"
    admin_preview = False

    def render(self, context, instance, placeholder):
        import uuid
        context['uuid'] = uuid.uuid4().hex[:4]  # allows for multiple onscreen
        max_width = 320 # an approximate width for the image - depends on the screensize of course
        max_width_mini_carousel = 480
        context['instance'] = instance
        context['display_as'] = instance.display_as
        if instance.content_group and instance.content_group._meta.many_to_many:
            m2m_fieldname = instance.content_group._meta.many_to_many[0].name
            context['item_list'] = getattr(instance.content_group, m2m_fieldname).all()
            context['flagship_margin_top_list'] = [(item.flagship_height and int(max(instance.height - item.flagship_height * min(1,max_width/item.flagship_width), 0)/2) or 0) for item in context['item_list'] ] 
            context['mini_flagship_margin_top_list'] = [(item.flagship_height and int(max(instance.height - item.flagship_height * min(1,max_width_mini_carousel/item.flagship_width), 0)/2) or 0) for item in context['item_list'] ] 
            for i in range(len(context['flagship_margin_top_list'])):
                context['item_list'][i].flagship_margin_top = context['flagship_margin_top_list'][i]
                context['item_list'][i].mini_flagship_margin_top = context['mini_flagship_margin_top_list'][i]
        return context

plugin_pool.register_plugin(RTCarouselPlugin)
