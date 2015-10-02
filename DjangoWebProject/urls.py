"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import *
from DjangoWebProject import settings
from django.contrib import admin
from app.views import Results, base, search, my_homepage_view
from app.forms import BootstrapAuthenticationForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.models import Units, University, Keywords


# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', my_homepage_view),
    url(r'^admin', include(admin.site.urls)),
    url(r'^index', my_homepage_view),
    url(r'^search', search),

    url(r'^results', Results.as_view()),


    #url(r'^results/(?P<pk>\d+)/', 'unit_detail', name='unit_detail'),

    #url(r'^login$',
    #    'django.contrib.auth.views.login',
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title':'Log in',
    #            'year':datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),



) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
