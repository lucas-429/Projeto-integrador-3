# meu_app/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth
from .models import Message

class MessagesByCategory(APIView):
    def get(self, request):
        counts = Message.objects.values('category').annotate(count=Count('id'))
        return Response(counts)

class MessagesByPeriod(APIView):
    def get(self, request):
        period = request.query_params.get('period', 'day')

        if period == 'day':
            counts = Message.objects.annotate(
                date=TruncDay('created_at')
            ).values('date').annotate(count=Count('id')).order_by('date')
        else:
            counts = Message.objects.annotate(
                date=TruncMonth('created_at')
            ).values('date').annotate(count=Count('id')).order_by('date')

        return Response(counts)