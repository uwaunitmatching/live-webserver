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


class Results(ListView):  
    template_name = 'results.html' 
    context_object_name = 'units'
    paginate_by = 10

    unit_found = None
    selected_keys = ""

    def get_related_units(self):
        unitTerm = self.request.GET.get('unit', '')
        univ_input = self.request.GET.get('university', '')
        univ = University.objects.extra(where=["%s LIKE uni_name"], params=[univ_input])
        selected_uni_id = univ[0].id
        print(selected_uni_id)
        selected_uni_name = univ[0].uni_name
        print(selected_uni_name)

        choose = Units.objects.all().extra(where=["%s LIKE unit_code"], params=[unitTerm])
        if choose[0].unit_name and choose[0].keywords:
            selected_unit_name = choose[0].unit_name
            global selected_keys
            selected_keys = choose[0].keywords
            unit_found = True
        else:
            selected_unit_name = "Sorry! Could not find your Unit"
            selected_keys = "Sorry! Keywords could not be found, Please refine your search"
            unit_found = None

        print(selected_unit_name)
        return choose


    def get_queryset(self):
        unitTerm = self.request.GET.get('unit', '')
        queryset = self.get_related_units()


        count_keywords = {}
        # count_keywords[id] = number of times all keywords show up in unit_desc
        count_keywords[11] = 14

        for key in selected_keys.split(','):
            if key:
                print(key)



        # for p in University.objects.raw("""
        #     SELECT DISTINCT app_units.id, app_university.uni_name 
        #     FROM app_units
        #     INNER JOIN app_university ON (app_units.uni_id = app_university.id)
        #     """):
        #     print("University: %s" % p)

        return queryset

    def get_context_data(self, **kwargs):
        unitTerm = self.request.GET.get('unit', '')
        univ_input = self.request.GET.get('university', '')

        context = super(ListView, self).get_context_data(**kwargs)
        context['unit'] = unitTerm
        context['university'] = univ_input
        context['request'] = self.request


        context['keys_list'] = selected_keys
        

        return context

def base(request):
    return render_to_response('base.html', locals(), context_instance = RequestContext(request))


def search(request):
    context = {'form' : searchForm}
    return render(request, 'search.html', context)

def login(request):
    return render_to_response('admin.html', locals(), context_instance = RequestContext(request))
