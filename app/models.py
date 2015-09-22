"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Units(models.Model):
    unit_key = models.IntegerField()
    uni_id = models.IntegerField()
    unit_code = models.CharField(max_length=20)
    unit_name = models.CharField(max_length=300)
    unit_desc = models.CharField(max_length=5000)
    unit_text = models.CharField(max_length=400)
    ISBN = models.IntegerField()
    FreeTags = models.CharField(max_length=5000)
    Positive = models.CharField(max_length=5000)
    unit_link = models.URLField(max_length=2084)
    def __unicode__(self):
        return self.unit_name

class University(models.Model):
	uni_id = models.IntegerField()
	uni_name = models.CharField(max_length=255)
	city = models.CharField(max_length=25)
	country = models.CharField(max_length=25)
	region = models.CharField(max_length=25)
	times_ranking = models.CharField(max_length=12)
	uni_link = models.URLField(max_length=2084)
	def __unicode__(self):
		return self.uni_name

class Keywords(models.Model):
	unit_key = models.IntegerField()
	keyword = models.CharField(max_length=32)
	def __unicode__(self):
		return self.keyword