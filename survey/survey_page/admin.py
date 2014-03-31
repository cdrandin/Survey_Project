from django.contrib import admin
from survey_page.models import *

##
## Event admin display and functionality changes
##

class SurveyPageAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'description', 'video_link', 'link']
	ordering = ['name']
	#list_filter = ['id', 'name']
	search_fields = ['description']
	#actions = ['make_published', make_drafted]
	fieldsets = [
        ('Name',                 {'fields': ['name']}),
        ('Survey Description', {'fields': ['description']}),
        ('Survey Technical  ', {'fields': ['link', 'video_link']}),
    ]

admin.site.register(SurveyPage, SurveyPageAdmin)