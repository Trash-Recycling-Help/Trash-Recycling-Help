# Import Calendar and datetime modules
from ics import Calendar, Event, DisplayAlarm
from datetime import datetime, timedelta 

# Function to create alarmed event and add to calendar
def addevent(calendar, name, begin):
    a = DisplayAlarm()
    a.trigger = timedelta(minutes = -1) 
    e0 = Event(alarms=[a])
    e0.name = name
    e0.begin = begin
    calendar.events.add(e0)

# Create calendar
c = Calendar()

# Add specific calendar events
# January
addevent(c,"Take out the trash and recycling!", '2021-01-03 22:01:00')
addevent(c,"Take out only the trash!", '2021-01-10 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-01-17 22:01:00')
addevent(c,"Take out only the trash!", '2021-01-24 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-01-31 22:01:00')
# February
addevent(c,"Take out only the trash!", '2021-02-07 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-02-14 22:01:00')
addevent(c,"Take out only the trash!", '2021-02-21 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-02-28 22:01:00')
# March
addevent(c,"Take out only the trash!", '2021-03-07 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-03-14 22:01:00')
addevent(c,"Take out only the trash!", '2021-03-21 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-03-28 22:01:00')
# April
addevent(c,"Take out only the trash!", '2021-04-04 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-04-11 22:01:00')
addevent(c,"Take out only the trash!", '2021-04-18 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-04-25 22:01:00')
# May
addevent(c,"Take out only the trash!", '2021-05-02 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-05-09 22:01:00')
addevent(c,"Take out only the trash!", '2021-05-16 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-05-23 22:01:00')
addevent(c,"Memorial Day: don't take out the trash today.", '2021-05-30 22:01:00')
# June
addevent(c,"Holiday makeup service: Take out only the trash!", '2021-06-01 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-06-06 22:01:00')
addevent(c,"Take out only the trash!", '2021-06-13 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-06-20 22:01:00')
addevent(c,"Take out only the trash!", '2021-06-27 22:01:00')
# July
addevent(c,"Take out the trash and recycling!", '2021-07-04 22:01:00')
addevent(c,"Take out only the trash!", '2021-07-11 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-07-18 22:01:00')
addevent(c,"Take out only the trash!", '2021-07-25 22:01:00')
# August
addevent(c,"Take out the trash and recycling!", '2021-08-01 22:01:00')
addevent(c,"Take out only the trash!", '2021-08-08 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-08-15 22:01:00')
addevent(c,"Take out only the trash!", '2021-08-21 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-08-29 22:01:00')
# September
addevent(c,"Labor Day: don't take the trash out today.", '2021-09-05 22:01:00')
addevent(c, "Holiday makeup service: Take out only the trash!", '2021-09-07 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-09-12 22:01:00')
addevent(c,"Take out only the trash!", '2021-09-19 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-09-26 22:01:00')
# October
addevent(c,"Take out only the trash!", '2021-10-03 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-10-10 22:01:00')
addevent(c,"Take out only the trash!", '2021-10-17 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-10-24 22:01:00')
addevent(c,"Take out only the trash!", '2021-10-31 22:01:00')
# November
addevent(c,"Take out the trash and recycling!", '2021-11-07 22:01:00')
addevent(c,"Take out only the trash!", '2021-11-14 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-11-21 22:01:00')
addevent(c,"Take out only the trash!", '2021-11-28 22:01:00')
# December
addevent(c,"Take out the trash and recycling!", '2021-12-05 22:01:00')
addevent(c,"Take out only the trash!", '2021-12-12 22:01:00')
addevent(c,"Take out the trash and recycling!", '2021-12-19 22:01:00')
addevent(c,"Take out only the trash!", '2021-12-26 22:01:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\my.ics', 'w') as my_file:
    my_file.writelines(c)