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

	return render(request, 'survey_query.html', {'survey_name': survey.name,
												 'youtube_link': survey.video_link,
												 'description': survey.description,
												 'survey_link': survey.link,
												 'count': survey.participation_count})