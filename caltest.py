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


#
# SE Quadrant
#

# Create calendar
seCal = Calendar()

# Add specific calendar events
# January
addevent(seCal,"Take out the trash and recycling!", '2021-01-03 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-01-10 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-01-17 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-01-24 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-01-31 22:01:00')
# February
addevent(seCal,"Take out only the trash!", '2021-02-07 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-02-14 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-02-21 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-02-28 22:01:00')
# March
addevent(seCal,"Take out only the trash!", '2021-03-07 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-03-14 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-03-21 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-03-28 22:01:00')
# April
addevent(seCal,"Take out only the trash!", '2021-04-04 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-04-11 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-04-18 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-04-25 22:01:00')
# May
addevent(seCal,"Take out only the trash!", '2021-05-02 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-05-09 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-05-16 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-05-23 22:01:00')
addevent(seCal,"Memorial Day: don't take out the trash today.", '2021-05-30 22:01:00')
# June
addevent(seCal,"Holiday makeup service: Take out only the trash!", '2021-06-01 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-06-06 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-06-13 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-06-20 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-06-27 22:01:00')
# July
addevent(seCal,"Take out the trash and recycling!", '2021-07-04 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-07-11 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-07-18 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-07-25 22:01:00')
# August
addevent(seCal,"Take out the trash and recycling!", '2021-08-01 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-08-08 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-08-15 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-08-22 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-08-29 22:01:00')
# September
addevent(seCal,"Labor Day: don't take the trash out today.", '2021-09-05 22:01:00')
addevent(seCal, "Holiday makeup service: Take out only the trash!", '2021-09-07 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-09-12 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-09-19 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-09-26 22:01:00')
# October
addevent(seCal,"Take out only the trash!", '2021-10-03 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-10-10 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-10-17 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-10-24 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-10-31 22:01:00')
# November
addevent(seCal,"Take out the trash and recycling!", '2021-11-07 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-11-14 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-11-21 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-11-28 22:01:00')
# December
addevent(seCal,"Take out the trash and recycling!", '2021-12-05 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-12-12 22:01:00')
addevent(seCal,"Take out the trash and recycling!", '2021-12-19 22:01:00')
addevent(seCal,"Take out only the trash!", '2021-12-26 22:01:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\seCal.ics', 'w') as my_file:
    my_file.writelines(seCal)


#
# NW Quadrant
#

# Create calendar
nwCal = Calendar()

# Add specific calendar events
# January
addevent(nwCal,"Take out the trash and recycling!", '2021-01-04 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-01-11 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-01-18 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-01-25 22:01:00')
# February
addevent(nwCal,"Take out the trash and recycling!", '2021-02-01 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-02-08 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-02-15 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-02-22 22:01:00')
# March
addevent(nwCal,"Take out the trash and recycling!", '2021-03-01 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-03-08 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-03-15 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-03-22 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-03-29 22:01:00')
# April
addevent(nwCal,"Take out only the trash!", '2021-04-05 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-04-12 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-04-19 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-04-26 22:01:00')
# May
addevent(nwCal,"Take out only the trash!", '2021-05-03 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-05-10 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-05-17 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-05-24 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-05-31 22:01:00')
# June
addevent(nwCal,"Take out the trash and recycling!", '2021-06-07 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-06-14 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-06-21 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-06-28 22:01:00')
# July
addevent(nwCal,"Take out the trash and recycling!", '2021-07-05 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-07-12 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-07-19 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-07-26 22:01:00')
# August
addevent(nwCal,"Take out the trash and recycling!", '2021-08-02 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-08-09 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-08-16 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-08-23 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-08-30 22:01:00')
# September
addevent(nwCal,"Take out only the trash!", '2021-09-06 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-09-13 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-09-20 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-09-27 22:01:00')
# October
addevent(nwCal,"Take out only the trash!", '2021-10-04 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-10-11 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-10-18 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-10-25 22:01:00')
# November
addevent(nwCal,"Take out only the trash!", '2021-11-01 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-11-08 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-11-15 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-11-22 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-11-29 22:01:00')
# December
addevent(nwCal,"Take out the trash and recycling!", '2021-12-06 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-12-13 22:01:00')
addevent(nwCal,"Take out the trash and recycling!", '2021-12-20 22:01:00')
addevent(nwCal,"Take out only the trash!", '2021-12-27 22:01:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\nwCal.ics', 'w') as my_file:
    my_file.writelines(nwCal)


#
# NE Quadrant
#

# Create calendar
neCal = Calendar()

# Add specific calendar events
# January
addevent(neCal,"Take out only the trash!", '2021-01-06 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-01-13 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-01-20 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-01-27 22:01:00')
# February
addevent(neCal,"Take out only the trash!", '2021-02-03 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-02-10 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-02-17 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-02-24 22:01:00')
# March
addevent(neCal,"Take out only the trash!", '2021-03-03 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-03-10 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-03-17 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-03-24 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-03-31 22:01:00')
# April
addevent(neCal,"Take out the trash and recycling!", '2021-04-07 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-04-14 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-04-21 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-04-28 22:01:00')
# May
addevent(neCal,"Take out the trash and recycling!", '2021-05-05 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-05-12 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-05-19 22:01:00')
addevent(neCal,"Take out only the trash!.", '2021-05-26 22:01:00')
# June
addevent(neCal,"Take out the trash and recycling!", '2021-06-02 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-06-09 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-06-16 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-06-23 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-06-30 22:01:00')
# July
addevent(neCal,"Take out only the trash!", '2021-07-07 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-07-14 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-07-21 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-07-28 22:01:00')
# August
addevent(neCal,"Take out only the trash!", '2021-08-04 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-08-11 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-08-18 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-08-25 22:01:00')
# September
addevent(neCal,"Take out only the trash!", '2021-09-01 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-09-08 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-09-15 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-09-22 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-09-29 22:01:00')
# October
addevent(neCal,"Take out the trash and recycling!", '2021-10-06 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-10-13 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-10-20 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-10-27 22:01:00')
# November
addevent(neCal,"Take out the trash and recycling!", '2021-11-03 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-11-10 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-11-17 22:01:00')
addevent(neCal,"Thanksgiving Day: don't take out the trash today.", '2021-11-24 22:01:00')
addevent(neCal, "Holiday makeup service: take out only the trash!", '2021-11-26 22:01:00')
# December
addevent(neCal,"Take out the trash and recycling!", '2021-12-01 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-12-08 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-12-15 22:01:00')
addevent(neCal,"Take out only the trash!", '2021-12-22 22:01:00')
addevent(neCal,"Take out the trash and recycling!", '2021-12-29 22:01:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\neCal.ics', 'w') as my_file:
    my_file.writelines(neCal)


#
# SW Quadrant
#

# Create calendar
swCal = Calendar()

# Add specific calendar events
# January
addevent(swCal,"Take out only the trash!", '2021-01-07 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-01-14 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-01-21 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-01-28 22:01:00')
# February
addevent(swCal,"Take out only the trash!", '2021-02-04 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-02-11 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-02-18 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-02-25 22:01:00')
# March
addevent(swCal,"Take out only the trash!", '2021-03-04 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-03-11 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-03-18 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-03-25 22:01:00')
# April
addevent(swCal,"Take out only the trash!", '2021-04-01 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-04-08 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-04-15 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-04-22 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-04-29 22:01:00')
# May
addevent(swCal,"Take out the trash and recycling!", '2021-05-06 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-05-13 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-05-20 22:01:00')
addevent(swCal,"Take out only the trash!.", '2021-05-27 22:01:00')
# June
addevent(swCal,"Take out the trash and recycling!", '2021-06-03 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-06-10 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-06-17 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-06-24 22:01:00')
# July
addevent(swCal,"Take out the trash and recycling!", '2021-07-01 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-07-08 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-07-15 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-07-22 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-07-29 22:01:00')
# August
addevent(swCal,"Take out only the trash!", '2021-08-05 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-08-12 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-08-19 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-08-26 22:01:00')
# September
addevent(swCal,"Take out only the trash!", '2021-09-02 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-09-09 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-09-16 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-09-23 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-09-30 22:01:00')
# October
addevent(swCal,"Take out the trash and recycling!", '2021-10-07 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-10-14 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-10-21 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-10-28 22:01:00')
# November
addevent(swCal,"Take out the trash and recycling!", '2021-11-04 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-11-11 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-11-18 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-11-25 22:01:00')
# December
addevent(swCal,"Take out the trash and recycling!", '2021-12-02 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-12-09 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-12-16 22:01:00')
addevent(swCal,"Take out only the trash!", '2021-12-23 22:01:00')
addevent(swCal,"Take out the trash and recycling!", '2021-12-30 22:01:00')

# Writing calendar file to disk
with open('..\\trash-recyling-help.github.io\\swCal.ics', 'w') as my_file:
    my_file.writelines(swCal)