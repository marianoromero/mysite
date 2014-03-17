from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.main', name='main'),
    url(r'^test/', 'blog.views.vistaTest', name='vistaTest'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include(admin.site.urls)),
)

#urlpatterns=patterns('blog.views',(r"","main"))