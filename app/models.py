"""
Definition of models.
"""

from django.db import models

# Create your models here.


class University(models.Model):
	uni_id = models.primary_key=True
	uni_name = models.CharField(max_length=255)
	city = models.CharField(max_length=25, null=True)
	country = models.CharField(max_length=25, null=True)
	region = models.CharField(max_length=25, null=True)
	times_ranking = models.CharField(max_length=12, null=True)
	uni_link = models.URLField(max_length=2084)
	def __unicode__(self):
		return self.uni_name

class Units(models.Model):
    unit_key = models.primary_key=True
    uni_id = models.IntegerField()
    unit_code = models.CharField(max_length=20, null=True)
    unit_name = models.CharField(max_length=300, null=True)
    unit_desc = models.CharField(max_length=5000, null=True)
    unit_text = models.CharField(max_length=400, null=True)
    ISBN = models.IntegerField(null=True)
    FreeTags = models.CharField(max_length=5000, null=True)
    Positive = models.CharField(max_length=5000, null=True)
    unit_link = models.URLField(max_length=2084, null=True)
    def __unicode__(self):
        return self.unit_name

class Keywords(models.Model):
	unit_key = models.IntegerField()
	keyword = models.CharField(max_length=32)
	def __unicode__(self):
		return self.keyword