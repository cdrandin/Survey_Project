from django.conf.urls import patterns, url
from survey_page import views

urlpatterns = patterns('',
	url(r'^$', views.app_main, name='app_main'),
) 