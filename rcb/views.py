from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kholi(request):
    return HttpResponse(' king kholi is a good batesman')