from django.db import models
from django.forms import ModelForm, Textarea

###
# Create table like this ... 
# python manage.py sql survey_page
# python manage.py syncdb
###

class SurveyPage(models.Model):
	name = models.CharField(max_length = 40)
	link  = models.CharField(max_length = 50)
	description =  models.TextField(null = True)
	video_link = models.CharField(max_length = 60, null = True)
	participation_count = models.IntegerField(default = 0)

	def __unicode__(self):
		return u'id:%s name:%s' % (self.id, self.name)

class SurveyPageForm(ModelForm):
	class Meta:
		model = SurveyPage
