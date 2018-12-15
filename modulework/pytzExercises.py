import pytz
import datetime

country_timezones = sorted(pytz.all_timezones)
country_codes = sorted(pytz.country_names)

for country in country_codes:
    timezone = pytz.country_timezones.get(country)
    local_Time_Str = "\n\tLocal Times of {}:\n".format(pytz.country_names[country])

    if timezone is None:
        local_Time_Str = "\n\tNo local time is available for {}\n".format(pytz.country_names[country])
    else:
        count = 0
        for local_zone in timezone:
            count += 1
            local_Time_Str += "\t" + str(count) + ".\t" + str(local_zone) + ": "
            tz_to_display = pytz.timezone(local_zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            local_Time_Str += local_time.strftime("%I:%M:%S %p - %x") + "\n"

    print("{0:^5}:\t{1:30}\t{2:50}".
          format(country, pytz.country_names[country], local_Time_Str))




