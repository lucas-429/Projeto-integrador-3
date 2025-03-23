"""
URL configuration for site_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from meu_app import views, api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('send_message/', views.send_message, name='send_message'),
    path('api/messages/by-category/', api_views.MessagesByCategory.as_view(), name='messages_by_category'),
    path('api/messages/by-period/', api_views.MessagesByPeriod.as_view(), name='messages_by_period'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
