from django.urls import path
from app_exchange.views import ConvertView

urlpatterns = [
    path('', ConvertView.as_view(), name='convert')
]
