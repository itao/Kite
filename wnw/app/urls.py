from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^app$', 'app.views.app', name='app'),
    url(r'^admin/', include(admin.site.urls)),
)
