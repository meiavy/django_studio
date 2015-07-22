from django.conf.urls import patterns, include, url

from django.contrib import admin
from django_studio.views import current_datetime

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_studio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^current_datetime/', current_datetime),
)
