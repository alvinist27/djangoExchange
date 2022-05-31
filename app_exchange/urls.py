from django.urls import path
from app_exchange.views import convert_view

urlpatterns = [
    path('', convert_view, name='convert')
]
