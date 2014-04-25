# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from survey_page.models import *

def app_main(request):
	# Gets current path
	#root_url = request.path.split('/apps/')[0]
	#return HttpResponseRedirect(root_url + '/apps/test/')

	return render(request, 'app_main.html', {})

def survey_query(request, survey_id):
	try:
		survey = SurveyPage.objects.get(pk=survey_id)
	except:
		return HttpResponse("Page does not exist")

	# Ugly way to get rid of ',' ';'' and break into nice pieces of (name, value)
	chart = list()
	temp  = ""
	# Parse data
	for data in survey.chart_encoding.replace(',', ' ').replace(';', ' ').split(' '):
		# We got a number put previously read words into the chart list as (word, number)
		if(data.isdigit()):
			chart.append([temp.strip(' '), data])
			temp = ""
		# Not number, Just append word to previous word
		else:
			temp += (" " + data)

	return render(request, 'survey_query.html', {'survey_name': survey.name,
												 'youtube_link': survey.video_link,
												 'description': survey.description,
												 'survey_link': survey.link,
												 'count': survey.participation_count,
												 'values': chart})

def google_charts_test(request):
	return render(request, 'google_charts_test.html', {'values': [['food', 32], ['stuff', 50]]})
