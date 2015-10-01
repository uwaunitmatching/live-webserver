from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader, RequestContext, Library, Node, TemplateSyntaxError
from app.models import Units, University, Keywords
from app.forms import searchForm
import sys

def my_homepage_view(request):
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

# @register.filter(name='get_range') 
# def get_range(value):
#     print value
#     return range(value)


def results(request):
    t = loader.get_template('results.html')
    form = searchForm(request.POST)

    if request.method == 'POST' and form.isValid():
        unit = form.unit
        university = form.university
        results = Units.objects.filter(unit_code__contains=unit)

    else:
        context = {'form' : searchForm}
        return render(request, 'search.html', context)
    
    queryset = Units.objects.all()
    # print([p.unit_name for p in queryset]) # Evaluate the query set.
    # print([p.unit_code for p in queryset]) #cached the query, reuse


    for unit in results:

        c = Context({
                # 'get_range' : get_range,
                'unit_name': unit.unit_name,
                'unit_desc': unit.unit_desc,
            })

    return render(request, "results.html", c)



def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    context = {'form' : searchForm}
    return render(request, 'search.html', context)

def login(request):
    return render_to_response('admin.html', locals(), context_instance = RequestContext(request))
