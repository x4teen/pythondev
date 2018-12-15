import time
print("System Start: ", time.strftime('%c', time.gmtime(0)))
print("Your current timezone is {0} with an offset of {1}"
      .format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("Daylight saving time is in effect")
else:
    print("Daylight saving time is not in effect")