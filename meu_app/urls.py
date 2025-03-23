# meu_app/urls.py
from django.urls import path
from . import api_views, views

urlpatterns = [
    path('api/messages/by-category/', api_views.MessagesByCategory.as_view(), name='messages_by_category'),
    path('api/messages/by-period/', api_views.MessagesByPeriod.as_view(), name='messages_by_period'),
]