from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vandana(request):
    return HttpResponse('<h1><marquee>Good morning to All....</h1></marquee>')
