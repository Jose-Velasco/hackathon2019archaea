from django.db import models

class Neighborhood(models.Model):
	name = models.CharField(blank=False, max_length=1000)
	def __str__(self):
		return self.name

class Location(models.Model):
	street_name = models.CharField(blank=False, max_length=1000)
	neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
	def __str__(self):
		return self.street_name

class Issue(models.Model):
	issue_type = models.CharField(blank=False, max_length=1000)
	next_date = models.DateField(null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	avg_dur = models.IntegerField(null=True)
	date_modified = models.DateField()
	def __str__(self):
		return self.issue_type + " on " + self.location.street_name

class Date(models.Model):
	date = models.DateField(blank=False)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

class Alert(models.Model):
	enabled = models.BooleanField(default=True)
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	message = models.CharField(blank=False, max_length=1000)
	start_date = models.DateField()
	end_date = models.DateField()