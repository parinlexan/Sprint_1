time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
new_time_string = time_string.replace(',', ' ')
time_list = new_time_string.split(' ')

mins_sum = 0

mins_list = []
hours_list = []
secs_list = []

for time_particle in time_list:
    if 's' in time_particle:
        secs_list.append(time_particle)
    elif 'h' in time_particle:
        hours_list.append(time_particle)
    else:
        mins_list.append(time_particle)

print(secs_list, hours_list, mins_list)

for sec in range(len(secs_list)):
    secs_list[sec] = int(secs_list[sec].replace('s', '')) / 60
    mins_sum += secs_list[sec]

for hour in range(len(hours_list)):
    hours_list[hour] = int(hours_list[hour].replace('h', '')) * 60
    mins_sum += hours_list[hour]

for min in range(len(mins_list)):
    mins_list[min] = int(mins_list[min].replace('m', ''))
    mins_sum += mins_list[min]

print(secs_list, hours_list, mins_list)

print(mins_sum)