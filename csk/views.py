from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ms(request):
    return HttpResponse(' ms is a good teamleader')