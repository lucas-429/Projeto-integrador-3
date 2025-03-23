from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer

def home(request):
    return render(request, 'home.html')

# Create your views here.
@csrf_protect
def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        category = request.POST['category']
        content = request.POST['content']

        message = Message(email=email, category=category, content=content, name=name)
        message.save()

        return redirect('home')  # Redirect to the home page after saving the message
    return render(request, 'home.html')


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

# meu_app/views.py
def dashboard(request):
    return render(request, 'dashboard.html')