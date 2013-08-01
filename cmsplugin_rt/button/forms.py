from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import ButtonPluginModel
from django import forms
from cms.models import Page


class ButtonForm(ModelForm):
    page_link = forms.ModelChoiceField(label=_("page"), 
                                       queryset=Page.objects.drafts(), 
                                       help_text=_("A link to a page overrides the above button link."),
                                       required=False)
    
    class Meta:
        model = ButtonPluginModel
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')