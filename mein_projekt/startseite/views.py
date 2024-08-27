from django.shortcuts import render
from django.http import HttpResponse

def hallo_view(request):
    return HttpResponse("Hallo, Welt!")
