from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .forms import ConverterForm
import requests


@cache_page(300)
def convert_view(request):
    response = requests.get('https://api.exchangerate.host/latest?base=USD').json()
    rates = response.get('rates')
    choices = [(choice, choice) for choice in rates]

    if request.method == 'GET':
        form = ConverterForm()
        form.fields['from_choice'].choices = choices
        form.fields['to_choice'].choices = choices

    elif request.method == 'POST':
        form = ConverterForm(request.POST)
        form.fields['from_choice'].choices = choices
        form.fields['to_choice'].choices = choices

        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            from_choice = form.cleaned_data.get('from_choice')
            to_choice = form.cleaned_data.get('to_choice')

            result = round(amount * (rates[to_choice] / rates[from_choice]), 2)
            return render(request, 'app_exchange/convert.html',
                          {'form': form, 'result': result})

    return render(request, 'app_exchange/convert.html', {'form': form})