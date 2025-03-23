from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'category', 'created_at','content')
    search_fields = ('email', 'category', 'created_at','content')