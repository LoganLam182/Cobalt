from django.http import HttpResponse
from django.shortcuts import render

def cobalt (request):
    #return HttpResponse("Hello world")
    return render(request, 'homepage.html')

def calendar (request):
    return render(request, 'cobalt_calendar.html')

def info (request):
    return render(request, "information_page.html")