from django import forms
from django.utils.translation import gettext_lazy as _


class ConverterForm(forms.Form):
    amount = forms.FloatField(label=_('Amount'), min_value=0, max_value=1e+30, required=True)
    from_choice = forms.ChoiceField(label=_('From'), initial='USD', required=True)
    to_choice = forms.ChoiceField(label=_('To'), initial='EUR', required=True)