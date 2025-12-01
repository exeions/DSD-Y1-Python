screen_times = [120, 95, 140, 160, 80, 100, 200]

day_1 = screen_times[0]
day_2 = screen_times[1]
day_3 = screen_times[2]

avg = (day_1+day_2+day_3)/3

print(day_3) ## Day 3
print(round(avg, 2)) ## Average
screen_times[-1] = 50 ## Last value change
print(max(screen_times), min(screen_times)) ## Highest and Lowest value
