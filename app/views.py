from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpRequest, HttpResponse, Http404
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

        try:
            univ = University.objects.extra(where=["%s LIKE uni_name"], params=[univ_input])
            selected_uni_id = univ[0].id
            print(selected_uni_id)
            selected_uni_name = univ[0].uni_name
            print(selected_uni_name)
        except IndexError:
            raise Http404("Sorry! University Not found. Please refine your search")

        
        try:
            choose = Units.objects.all().extra(where=["%s LIKE unit_code"], params=[unitTerm])
            selected_unit_name = choose[0].unit_name
            global selected_keys
            selected_keys = choose[0].keywords
            unit_found = True
        except IndexError:
            raise Http404("Sorry! Your unit could not be found. Please refine your search")

        print(selected_unit_name)
        return choose


    def get_queryset(self):
        unitTerm = self.request.GET.get('unit', '')
        goodset = self.get_related_units()


        count_keywords = {}
        # count_keywords[id] = number of times all keywords show up in unit_desc

        #only get the first 15 keywords, keep queries fast
        units = Units.objects.all()

        num_keywords = 0
        for key in selected_keys.split(','):
            if key and num_keywords < 15:
                num_keywords+=1

                for k in key.split(' '):
                    num_times_appeared = 0

                    #key is all individual keywords
                    # print(k)

                    #for each keyword, query the database and .count() the number of times
                    #it appears in each 
                    for unit in units:
                        num_times_appeared = 0
                        # print("Searching in", unit.unit_name, unit.id)
                        if(unit.unit_desc and unit.id and unit.unit_name):
                            if(unit.unit_desc.count(k) > 0):
                                num_times_appeared += unit.unit_desc.count(k)

                            # print(num_times_appeared)
                            if(count_keywords.get(unit.id)):
                                count_keywords[unit.id] = count_keywords.get(unit.id) + num_times_appeared
                            else:
                                count_keywords[unit.id] = 0 + num_times_appeared
                        else:
                            break


        ordered_result_list = []
        #sorting according to values
        for unit in sorted(count_keywords, key=count_keywords.get, reverse=True):
            # print unit, count_keywords[unit]
            ordered_result_list.append(unit)

        queryset = units.filter(pk__in=ordered_result_list)
        return queryset


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
