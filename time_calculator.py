def add_time(start, duration, day=None):

	days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

	initialtime = list(map(int, start[:-3].split(':')))
	duration = list(map(int, duration.split(':')))

    #adding MINUTES to initial time, resets minutes to 0 when intial time goes above 60 and adds count
	initialtime[1] += duration[1]
	count = 0 
	while initialtime[1] > 60:
	    count += 1
	    initialtime[1] -= 60
    
    #hours
	initialtime[0] += count + duration[0]
	count = 0
	while initialtime[0] >= 12:
	    initialtime[0] -= 12
	    #when hours goes above 12 and its PM, add count to number of days and change to AM
	    if 'PM' in start:
	        count += 1 
	        start = start.replace('PM', 'AM')
	    elif 'AM' in start:
	        start = start.replace('AM', 'PM')

    #if hour is 0 then set hours to 12, if not leave as the hour in string
	initialtime[0] = '12' if initialtime[0] == 0 else str(initialtime[0])
	initialtime[1] = str(initialtime[1]).rjust(2, '0')
	new_time = ':'.join(initialtime) + start[-3:]
	
	if day is not None:
	    day = day.lower().capitalize()
	    days = days[days.index(day):] + days[:days.index(day)]
	    n = count
	    while n > 7:
	        n -= 7
	    new_time += ', ' + days[n]
	
	if count == 1:
	    new_time += ' (next day)'
	elif count > 1:
	    new_time += ' (' + str(count) + ' days later)'
	
	return new_time