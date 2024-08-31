year = int(input().strip())

if year < 1 or year > 4000:
    raise ValueError('Year must be between 1 and 4000')

result = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    result = 1

print(result)

