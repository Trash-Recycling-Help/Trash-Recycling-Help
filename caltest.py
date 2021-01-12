from ics import Calendar, Event
c = Calendar()
e0 = Event()
e0.name = "Take out only the trash!"
e0.begin = '2021-01-12 23:30:00'
c.events.add(e0)
e1 = Event()
e1.name = "Take out the trash and recycling!"
e1.begin = '2021-01-12 23:40:00'
c.events.add(e1)
e2 = Event()
e2.name = "Take out only the trash!"
e2.begin = '2021-01-12 23:50:00'
c.events.add(e2)
with open('..\\trash-recyling-help.github.io\\my.ics', 'w') as my_file:
    my_file.writelines(c)