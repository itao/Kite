from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

def app(request):
    context = RequestContext(request)
    return render_to_response('app.html', context)
