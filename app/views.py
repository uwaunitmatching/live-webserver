from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader, RequestContext, Library, Node, TemplateSyntaxError
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    paginate_by = 10

    def get_queryset(self):
        unitTerm = self.request.GET.get('unit', '')
        queryset = Units.objects.filter(unit_code__icontains=unitTerm)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['unit'] = self.request.GET.get('unit', '') 
        context['university'] = self.request.GET.get('university', '') 
        context['request'] = self.request
        return context

def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    context = {'form' : searchForm}
    return render(request, 'search.html', context)

def login(request):
    return render_to_response('admin.html', locals(), context_instance = RequestContext(request))
