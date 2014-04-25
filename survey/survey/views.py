# Create your views here.
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

def root(request):
	return HttpResponse("You made it");