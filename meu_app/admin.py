# meu_app/admin.py
from django.contrib import admin
from django.urls import path
from .models import Message
from .views import dashboard
from django.contrib.auth.models import User

user = User.objects.get(username='admin')
user.is_staff = True
user.is_superuser = True
user.save()

class MyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(dashboard), name='dashboard'),
        ]
        return custom_urls + urls

admin_site = MyAdminSite(name='admin')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'category', 'created_at', 'content')
    search_fields = ('email', 'category', 'created_at', 'content')

admin_site.register(Message, MessageAdmin)
