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
addevent(c,"Take out only the trash!", '2021-01-13 19:16:00')
addevent(c,"Take out the trash and the recycling!", '2021-01-13 19:21:00')
addevent(c,"Take out only the trash!", '2021-01-13 19:26:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\my.ics', 'w') as my_file:
    my_file.writelines(c)