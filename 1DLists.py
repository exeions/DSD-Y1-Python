energy_levels = [6, 7, 1, 5, 2]

usernames = [
    "exeions",
    "deetux",
    "goombie",
    "cyrus",
    "weegeemantion",
    "ozzar",
    "kierxn",
    "DB095",
    "Vince",
    "mrballz",
    "dom_playz"]

step_count = [1253, 7524, 215, 167, 3235]

def findMiddleValue(list):
    length = len(list)
    if length%2 != 0:
        middle_index = length//2
        print(list[middle_index])
    else:
        first_middle_index = length // 2 - 1
        second_middle_index = length // 2
        print((list[first_middle_index], list[second_middle_index]))


energy_levels.append(9949248358435435435)
usernames.append("New value")
step_count.append(136444)


print(energy_levels, usernames, step_count)


print(energy_levels[0])
findMiddleValue(energy_levels)
print(energy_levels[-1])

print(usernames[0])
findMiddleValue(usernames)
print(usernames[-1])

print(step_count[0])
findMiddleValue(step_count)
print(step_count[-1])
