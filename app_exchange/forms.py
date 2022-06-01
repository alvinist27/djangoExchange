from django import forms


class ConverterForm(forms.Form):
    amount = forms.FloatField(min_value=0, max_value=1e+30, required=True)
    from_choice = forms.ChoiceField(label='From', initial='USD', required=True)
    to_choice = forms.ChoiceField(label='To', initial='EUR', required=True)