import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Local Time is {}".format(local_time.strftime('%c')))
print("UTC Time is {}".format(utc_time.strftime('%c')))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)
print("Aware local time {0:%c} and time zone is {1}"
      .format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time {0:%c} and time zone is {1}"
      .format(aware_utc_time, aware_utc_time.tzinfo))

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())
print()

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{0} seconds since the epoch is {1}".format(s, dt1))
print("{0} seconds since the epoch is {1}".format(t, dt2))