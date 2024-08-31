hour, minute = map(int, input().strip().split())
oven_minute = int(input().strip())

if hour < 0 or hour > 23:
    raise ValueError('hour must be between 0 and 23')
if minute < 0 or minute > 59:
    raise ValueError('minute must be between 0 and 59')
if oven_minute < 0 or oven_minute > 1000:
    raise ValueError('oven_minute must be between 0 and 1000')

total_minute = hour * 60 + minute
total_minute += oven_minute

cal_hour = total_minute // 60
cal_minute = total_minute % 60

if cal_hour >= 24:
    cal_hour -= 24

print(cal_hour, cal_minute)