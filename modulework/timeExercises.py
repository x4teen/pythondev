import time
from time import perf_counter as my_timer
import calendar
import random


time_format = "%I:%M:%S %p - %x"
time_GMT = time.gmtime()
time_here = time.localtime()
print("GMT: ", time.strftime(time_format, time_GMT))
print("Local Time:", time.strftime(time_format, time_here))
print("Local Time Zone: ", time.strftime("%Z", time_here))
print("Time as Floating Point: ", time.time())
print()

print("Year:", time_here[0])
print("Month:", time_here[1])
print("Day:", time_here[2])
print()

target_calendar = calendar.month(2018, 12)
print(target_calendar)

input("press enter to start")
wait_time = random.randint(1, 6)
start_time = my_timer()
input("press enter to stop")
end_time = my_timer()

time_format = "%I:%M:%S %p - %x"
print("Started: ", time.strftime(time_format, time.localtime(start_time)))
print("Stopped: ", time.strftime(time_format, time.localtime(end_time)))
print("Reaction Time: {0} seconds.".format(end_time-start_time))

print(time.get_clock_info('perf_counter'))

