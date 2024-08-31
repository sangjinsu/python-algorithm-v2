hour, minute = map(int, input().split())

if hour < 0 or hour > 25:
    raise ValueError('hour is not valid')

if minute < 0 or minute > 59:
    raise ValueError('minute is not valid')

if 45 <= minute:
    minute -= 45
else:
    hour -= 1
    minute += 15

    if hour < 0:
        hour += 24

print(hour, minute)
