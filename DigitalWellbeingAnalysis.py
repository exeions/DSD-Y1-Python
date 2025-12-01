notifications = [34, 28, 55, 40, 60, 22, 18]
notifcations2 = [57, 11, 72, 121, 71, 83, 19]

print(notifications[0])
print(notifications[1])
print(notifications[2])
print(notifications[3])
print(notifications[4])
print(notifications[5])
print(notifications[6])

## Calculates
highest_day = max(notifications)
lowest_day = min(notifications)
print(highest_day, lowest_day)

total_notifs = sum(notifications)
print(total_notifs)

avg = total_notifs/len(notifications)
print(round(avg, 2))

notifications.append(int(input("Input amount of notifications add: ")))
print(notifications)

total_notifs2 = sum(notifcations2)
if total_notifs > total_notifs2:
    diff = total_notifs - total_notifs2
    print(f"User 1 has {diff} more total notifications!")
else:
    diff = total_notifs2 - total_notifs
    print(f"User 2 has {diff} more total notifications!")