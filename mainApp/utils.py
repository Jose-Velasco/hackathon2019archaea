from datetime import date, timedelta

def generate_report():
	pass

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