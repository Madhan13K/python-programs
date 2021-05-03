import pytz
import datetime
print('the local time {}'.format(datetime.datetime.now()))
print('the utc time is {}'.format(datetime.datetime.utcnow()))
aware_time=pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
aware_utc_time=pytz.utc.localize(datetime.datetime.utcnow())
print('{} and {}'.format(aware_time,aware_time.tzinfo))
print('{} and {} '.format(aware_utc_time,aware_utc_time.tzinfo))

print( ' {} & {}'.format(datetime.datetime.now(),pytz.timezone('Asia/Kolkata').datetime.datetime.now(tz).tzname()))
