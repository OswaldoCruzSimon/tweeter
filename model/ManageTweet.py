import random 
from dateutil import rrule
from datetime import datetime, timedelta

#class ManageTweet:
def getCantTweet(banco, fecha_ini,fecha_fin,filtro):
	now = datetime.strptime('2017-03-15 12:00:00', '%Y-%m-%d %H:%M:%S') #datetime.now()
	hundredDaysLater = now + timedelta(days=5)
	data = []
	close = []
	for dt in rrule.rrule(rrule.HOURLY, dtstart=now, until=hundredDaysLater):
		data.append( dt.strftime("%Y-%m-%d %H:%M:%S") )
		close.append( str(random.uniform(1, 10)) )
	return {'date':date,'close':close}