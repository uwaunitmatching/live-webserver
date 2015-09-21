"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from DjangoWebProject import settings
from django.contrib import admin
from app.views import index, results, base, search
from app.forms import BootstrapAuthenticationForm
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin', include(admin.site.urls)),
    url(r'^index$', index),
    url(r'^results$', results),
    url(r'^search$', search),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),



) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
