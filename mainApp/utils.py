from datetime import date, timedelta
from .models import Neighborhood, Location, Date
#from django.core.mail import send_mail

def send_emails():
	pass

def check_for_new_alerts():
	neighborhoods = Neighborhood.objects.all()
	for n in neighborhoods:
		locations = n.location_set.all()
		for loc in locations:
			issues = loc.issue_set.all()
			for iss in issues:
				# check if there is already an existing alert about this issue
				if alert_exists(iss.id):
					continue
				duration = guess_duration(iss.next_date, 10)
				today = date.today()
				# Otherwise, create an alert if needed
				if today >= duration[0] and today <= duration[1]:
					generate_alert(iss.id, duration[0], duration[1])

# PARAMS: int alert_id, the id of the alert to disable
# RETURNS: NOTHING
def disable_alert(alert_id):
	if Alert.objects.filter(id=alert_id).exists():
		alert = Alert.objects.get(id=alert_id)
		alert.enabled = False
		alert.save()

def generate_alert(issue_id, start_day, end_day):
	iss = Issue.objects.get(id=issue_id)
	street_name = iss.location.street_name
	n_name = iss.location.neighborhood.name
	# Ex: 15TH AVE (Inner Richmond) is estimated to need Tree Maintenance attention between Oct 30 2019 and Nov 09 2019
	msg = street_name+" ("+n_name+") is estimated to need "+iss.issue_type+" attention between "+ start_day.strftime("%b %d %Y")+" and "+end_day.strftime("%b %d %Y")
	new_alert = Alert(
		issue=iss,
		message=msg,
		start_date=start_day,
		end_date=end_day
	)
	new_alert.save()

# PARAMS: int issue_id
# RETURNS: boolean, if an alert already exists about that issue
def alert_exists(issue_id):
	alerts = Alert.objects.all()
	for alert in alerts:
		if alert.issue.id == issue_id:
			return True
	return False

# PARAMS: list of dates, date_list
# RETURNS: timedelta, the average duration between each date
def avg_duration(date_list):
	if len(date_list) < 2:
		return 0
	durationCount = 1
	durationSum = date_list[1] - date_list[0]
	for i in range(2, len(date_list)):
		durationSum += (date_list[i] - date_list[i-1])
		durationCount += 1
	return (durationSum / durationCount)

# PARAMS: list of dates, date_list
# RETURNS: date next_date, an estimation of when something might attention
def predict_next(date_list):
	avg_dur = avg_duration(date_list)
	next_date = date_list[len(date_list)-1]+avg_dur
	return next_date

# PARAMS: date next_date, timedelta margin
# RETURNS: list of 2 dates, beginning and end
def guess_duration(next_date, margin):
	return [next_date - (margin / 2), next_date + (margin / 2)]

import csv

categories = [
	'Tree Maintenance',
	'Street Defects',
	'Streetlights',
	'Sidewalk or Curb',
]

def read_csv():
	with open("C:\\Users\\admin\\Desktop\\Projects\\Hackathon 2019\\311_Cases.csv", 'r', encoding="utf8") as csvf:
		for line in csvf:
			datareader = csv.reader(csvf, delimiter=',')
			for row in datareader:
				if row[7] in categories:
					itype = row[7]
					st = row[11]
					nbh = row[13]
					# Create neighborhood with name if it doesn't exist
					if not Neighborhood.objects.filter(name=nbh).exists():
						Neighborhood.objects.create(name=nbh)
					neighborhood = Neighborhood.objects.get(name=nbh)
					# Create location in neighborhood with street name if it doesn't exist
					if not Location.objects.filter(street_name=st, neighborhood=neighborhood).exists():
						Location.objects.create(street_name=st, neighborhood=neighborhood)
					loc = Location.objects.get(street_name=st, neighborhood=neighborhood)
					# Create issue at location with issue type if it doesn't exist
					if not Issue.objects.filter(location=loc, issue_type=itype).exists():
						Issue.objects.create(location=loc, issue_type=itype)
					iss = Issue.objects.get(location=loc, issue_type=itype)
					day = date.strptime(row[1], '%m/%d/%Y')
					# Create date object for issue with given date if it doesn't exist
					if not Date.objects.filter(date=day, issue=iss).exists():
						Date.objects.create(date=day, issue=iss)
					'''dateobj = Date.objects.get(date=day, issue=iss)'''

# 0 - CaseID (int)
# 1 - Opened (date)
# 2 - Closed (date)
# 3 - Updated (date)
# 4 - Status (string)
# 5 - Status Notes (string)
# 6 - Responsible Agency (string)
# 7 - Category (string)
# 8 - Request Type (string)
# 9 - Request Details ()
# 10 - Address
# 11 - Street
# 12 - Supervisor District
# 13 - Neighborhood
# 14 - Police District
# 15 - Latitude
# 16 - Longitude
# 17 - Point
# 18 - Source
# 19 - Media URL