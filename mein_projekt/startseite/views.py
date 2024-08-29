from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def hallo_view(request):
    template = loader.get_template('hallo.html')
    context = {
        'nachricht': 'Hallo, Welt!',
    }
    return HttpResponse(template.render(context, request))
   
