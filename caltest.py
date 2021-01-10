from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "Take out only the trash!"
e.begin = '2021-01-10 21:30:00'
c.events.add(e)
c.events
with open('my.ics', 'w') as my_file:
    my_file.writelines(c)