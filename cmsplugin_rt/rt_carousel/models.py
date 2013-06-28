# Plugin models

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.models.pluginmodel import CMSPlugin


CAROUSEL_DISPLAY_CHOICES = (
    ('bootstrap', _('Bootstrap carousel')),
    ('list', _('List')),
)

allowed_models = getattr(settings, 'ALLOWED_MODELS_IN_RT_CAROUSEL', [])
# ALLOWED_MODELS_IN_RT_CAROUSEL must be a list of dictionaries with keys:
#   app_label and model, e.g.
# ALLOWED_MODELS_IN_RT_CAROUSEL = [{'app_label':'sngapp', 'model':'gamegroup'},]
fk_models = None
if allowed_models:
    fk_models = models.Q(app_label = allowed_models[0]['app_label'].lower(), model = allowed_models[0]['model'].lower())
    for m in allowed_models[1:]:
        fk_models = fk_models | models.Q(app_label = m['app_label'].lower(), model = m['model'].lower())

class RTCarouselPluginModel(CMSPlugin):
    # content_group must point to a model with a ManyToMany field.
    # The Carousel will find this field and present the items in it.
    # Displaying the id as part of its description helps because
    # the admin panel will ask for the type and id directly.
    # e.g.
    # class GameGroup(models.Model):
    #     name = models.CharField(max_length=36)
    #     games = models.ManyToManyField(Game, through="GameGroupMember")
    #     def __unicode__(self):
    #         return "{0} (id {1})".format(self.name, self.id)
    #
    # and
    # class GameGroupMember(models.Model):
    #     group = models.ForeignKey(GameGroup)
    #     game = models.ForeignKey(Game)
    #     position = models.PositiveIntegerField(null=True, blank=True)

    content_type = models.ForeignKey(ContentType, limit_choices_to = fk_models)
    object_id = models.PositiveIntegerField()
    content_group = generic.GenericForeignKey('content_type', 'object_id')
    height = models.IntegerField(_("height"), default=480, help_text=_("Please enter height in pixels"))
    margin = models.CharField(_("margins"), max_length=50, blank=True, default="40px 0 40px 0", help_text=_("Please enter in css format: top right bottom left, e.g. 40px 0 40px 0"))
    display_as = models.CharField(max_length=30, default=CAROUSEL_DISPLAY_CHOICES[0][0], choices=CAROUSEL_DISPLAY_CHOICES)
    mini = models.BooleanField()
    animated = models.BooleanField(default=True)
    
    def __unicode__(self):
        return str(self.height) + u"px " + (self.animated and u"animated " or u"") + (self.mini and u"mini " or u"") + self.display_as
