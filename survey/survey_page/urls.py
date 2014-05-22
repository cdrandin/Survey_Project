from django.conf.urls import patterns, url
from survey_page import views
from django.conf import settings

# .../apps/ extention
urlpatterns = patterns('',
	url(r'^$', views.app_main, name='app_main'),
	url(r'^id/(\d+)$', views.survey_query, name='survey_query'),

    url(r'^test$', views.google_charts_test, name='google_charts_test'),
) 

'''
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
'''