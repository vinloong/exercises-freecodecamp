import re

Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, weekday=""):
    timeparts = re.split("[: ]", start)
    hour = int(timeparts[0])
    min = int(timeparts[1])
    if 'PM' == timeparts[2]:
        hour = hour + 12
    nums = re.split(':', duration)
    hours = int(nums[0])
    mins = int(nums[1])
    totols_min = min + mins
    min = totols_min % 60
    hour = hour + hours + (totols_min // 60)
    days = hour // 24
    hour = hour % 24
    ending = 'AM'
    if hour >= 12:
        ending = 'PM'
        if hour > 12:
            hour = hour - 12
    if hour == 0:
        hour = 12
        ending = 'AM'
    timestr = str.format("{}:{:02d} {}", hour, min, ending)
    if len(weekday.strip()) != 0:
        index = Weekday.index(weekday.capitalize())
        index = (index + days + 1) % 7
        timestr = str.format("{}, {}", timestr, Weekday[index - 1])
    if days > 1:
        timestr = str.format("{} ({} days later)", timestr, days)
    elif days == 1:
        timestr = str.format("{} (next day)", timestr)
    return timestr
