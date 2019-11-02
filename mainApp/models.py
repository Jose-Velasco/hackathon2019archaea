from django.db import models

class Location(models.Model):
	street_name = models.CharField(blank=False, max_length=1000)

class Issue(models.Model):
	issue_type = models.CharField(blank=False, max_length=1000)
	next_date = models.DateField(null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Date(models.Model):
	date = models.DateField(blank=False)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)