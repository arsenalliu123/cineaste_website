from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings
from cineaste import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(.*)$', views.search),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    )
