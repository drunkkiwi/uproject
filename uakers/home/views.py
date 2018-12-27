from django.shortcuts import render
from .models import Confessions

def home_view(request):
    all_conf = Confessions.objects.all().order_by('-id')

    context = {
        'all_conf': all_conf,
    }
    return render(request, 'home/home.html', context)
