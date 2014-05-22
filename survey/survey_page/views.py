# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from survey_page.models import *
import math

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

	# Resulting chart value is a list of list. Which each cell contains ["name", number]
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

	# Put values as string. Make it so the entered values line up to the correct values on the chart
	values  = ""
	prev_val = int(chart[0][1])
	values += chart[0][1] + "|"
	MAX = 0
	max_offset = 10
	for i in range(1, len(chart)):
		cur_val = int(chart[i][1])
		new_val = cur_val
		new_val -= prev_val
		prev_val = cur_val
		values  += str(new_val) + "|"
		if(i >= len(chart)-1):
			MAX = str(cur_val+max_offset)

	values  = values[:-1]

	# List of colors
	COLORS = ["0066FF", "00CC66", "5C8A00", "FFFF00", "FF9933", "FF0000", "990099", "66FFCC"]

	# How much to incr through the colors
	color_incr = int(math.ceil(len(COLORS)/len(chart)))
	#print(len(COLORS))
	#print(len(chart))
	#print(color_incr)

	# Put in colors as string
	color_string = ""
	for i in range(0, len(COLORS), color_incr):
		color_string += COLORS[i]
		if i <= len(COLORS)-1 - color_incr:
			color_string += ","

	# Put legends as string
	legends = ""
	for i in range(0, len(chart)):
		legends += str(chart[i][0]) + "|"
	legends = legends[:-1]

	google_charts_html_string = "http://chart.apis.google.com/chart?\
								cht=bvs&chs=350x300&chd=t:%s&\
								chxr=1,0,%s&chds=0,%s&\
								chco=%s&\
								chbh=60,20,60&\
								chxt=x,y&chxl=0:|survey and stuff&\
								chdl=%s&\
								chg=0,8.3,5,5" %(values, MAX, MAX, color_string, legends)
   
	return render(request, 'survey_query.html', {'survey_name' : survey.name,
												 'youtube_link': survey.video_link,
												 'description' : survey.description,
												 'survey_link' : survey.link,
												 'count'       : survey.participation_count,
												 'html'        : google_charts_html_string})

def google_charts_test(request):
	return render(request, 'google_charts_test.html', {'html': string})