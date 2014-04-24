from django.db import models
from django.forms import ModelForm, Textarea
from django.core.validators import RegexValidator
import re

###
# Create table like this ... 
# python manage.py sql survey_page
# python manage.py syncdb
###

RE = re.compile('([A-Za-z0-9]+\s*,\s*[0-9]+\s*;\s*)+')

class SurveyPage(models.Model):
	name                = models.CharField(max_length = 40)
	link                = models.CharField(max_length = 50)
	description         = models.TextField(null = True)
	video_link          = models.CharField(max_length = 60, null = True)
	participation_count = models.IntegerField(default = 0)

	chart_encoding      = models.CharField(max_length = 100, null = False, blank = False, 
										   validators=[RegexValidator(regex=RE, 
										   						      message="Inapproperiate chart econding! " + 
										   						      		  "Requires the format: {word} , {number} ;" +
										   						      		  " **Don't worry about spaces** " +
										   						      		  "(Ex. movie tickets, 50; more stuff, 100;)")],)

	def __unicode__(self):
		return u'id:%s name:%s' % (self.id, self.name)

class SurveyPageForm(ModelForm):
	class Meta:
		model = SurveyPage
