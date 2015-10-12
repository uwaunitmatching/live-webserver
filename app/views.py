﻿from django.shortcuts import render, render_to_response, RequestContext
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


class Results(ListView):  
    template_name = 'results.html' 
    context_object_name = 'units'
    paginate_by = 10


    def get_queryset(self):

        unitTerm = self.request.GET.get('unit', '')
        # unitKeywords = Units.objects.filter('')

        queryset = Units.objects.filter(unit_code__icontains=unitTerm)
        # queryset.orderBy('count')


        keys = {}


        for e in queryset:
            keys[e.id] = e.keywords


        keyword_list = keys.values()
        for key in keyword_list:
            if key:
                for k in key.split(","):
                    print(k)


        # print(queryset)

        # for p in University.objects.raw("""
        #     SELECT DISTINCT app_units.id, app_university.uni_name 
        #     FROM app_units
        #     INNER JOIN app_university ON (app_units.uni_id = app_university.id)
        #     """):
        #     print("University: %s" % p)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        unitTerm = self.request.GET.get('unit', '')
        context['unit'] = unitTerm
        context['university'] = self.request.GET.get('university', '') 
        context['request'] = self.request
        context['unitkeys'] = Units.objects.filter(unit_code=unitTerm)
        

        return context

def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    context = {'form' : searchForm}
    return render(request, 'search.html', context)

def login(request):
    return render_to_response('admin.html', locals(), context_instance = RequestContext(request))
