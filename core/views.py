from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    challenges = Challenge.objects.all().order_by('-posted_at')
    return render(request, 'index.html',{'challenges':challenges})