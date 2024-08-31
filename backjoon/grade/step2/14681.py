x = int(input().strip())
y = int(input().strip())

if x < -1000 or x > 1000 or x == 0:
    raise ValueError('x is not valid')
if y < -1000 or y > 1000 or y == 0:
    raise ValueError('y is not valid')

result = 0
if x > 0 and y > 0:
    result = 1
elif x < 0 and y < 0:
    result = 3
elif x < 0 < y:
    result = 2
elif x > 0 > y:
    result = 4

print(result)