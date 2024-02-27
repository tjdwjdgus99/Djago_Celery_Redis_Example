# api/urls.py

from django.urls import path
from api.views import process_number_view

urlpatterns = [
    path('process_number/', process_number_view, name='process_number'),
]
