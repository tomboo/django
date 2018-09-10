from django.shortcuts import render
from .models import Weight


def home(request):
    context = {
        'weights': Weight.objects.all()
    }
    return render(request, 'monitor/home.html', context)
