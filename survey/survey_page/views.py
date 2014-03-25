# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

def app_main(request):
	# Gets current path
	#root_url = request.path.split('/apps/')[0]
	#return HttpResponseRedirect(root_url + '/apps/test/')

	return HttpResponse("app_main")