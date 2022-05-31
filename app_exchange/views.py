from django.shortcuts import render
from django.views import View


class ConvertView(View):
    def get(self, request):
        return render(request, 'app_exchange/convert.html')
