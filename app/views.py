from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader, RequestContext, Library, Node, TemplateSyntaxError
from django.views.generic import ListView, DetailView
from app.models import Units, University, Keywords
from app.forms import searchForm
import sys

def my_homepage_view(request):
    context = {'form' : searchForm}
    return render(request, 'index.html', context)

# @register.filter(name='get_range') 
# def get_range(value):
#     print value
#     return range(value)

class Results(ListView):  
    template_name = 'results.html' 
    context_object_name = 'units'

    def get_queryset(self):
        unitTerm = self.request.GET.get('unit', '')
        queryset = Units.objects.filter(unit_code__icontains=unitTerm)
        return queryset

    #if request.method == 'POST':
    #    form = searchForm(request.POST)
    #    if form.is_valid():
    #        unit = form.cleaned_data['unit']
    #        university = form.cleaned_data['university']
    #        queryset = Units.objects.filter(unit_code__contains='cits')

    #    else:
    #        context = {'form' : searchForm}
    #        return render(request, 'search.html', context)
    #else:
    #    context = {'form' : searchForm}
    #    return render(request, 'search.html', context)


#def Results(request):
#    template_name = 'results.html'
#    queryset = Units.objects.filter(unit_code__contains='cits')[:7]

#    if request.method == 'POST':
#        form = searchForm(request.POST)
#        if form.is_valid():
#            unit = form.cleaned_data['unit']
#            university = form.cleaned_data['university']
#            queryset = Units.objects.filter(unit_code__contains='cits')

#    #    else:
#    #        context = {'form' : searchForm}
#    #        return render(request, 'search.html', context)
#    #else:
#    #    context = {'form' : searchForm}
#    #    return render(request, 'search.html', context)

#    return render(request, "results.html", queryset)

def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    context = {'form' : searchForm}
    return render(request, 'search.html', context)

def login(request):
    return render_to_response('admin.html', locals(), context_instance = RequestContext(request))
