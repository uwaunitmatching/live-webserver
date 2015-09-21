from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader

def index(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def results(request):
    return render_to_response('results.html', locals(), context_instance = RequestContext(request))

def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    return render_to_response('search.html', locals(), context_instance = RequestContext(request))