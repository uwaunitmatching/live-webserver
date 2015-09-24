from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader, RequestContext, Library, Node, TemplateSyntaxError
from app.models import Units
import sys

def index(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

# @register.filter(name='get_range') 
# def get_range(value):
#     print value
#     return range(value)


def results(request):
    t = loader.get_template('results.html')
    print >> sys.stderr, repr(Units.objects.filter(unit_code__contains="CITS"))
    

    c = Context({
            # 'get_range' : get_range,
            'university_name': 'University of Western Australia',
            'unit_code' : 'CITS3200',
            'unit_name' : 'Professional Computing',
            'unit_desc' : 'Description of Professional computing.'
        })
    return render(request, "results.html", c)



def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    return render_to_response('search.html', locals(), context_instance = RequestContext(request))

