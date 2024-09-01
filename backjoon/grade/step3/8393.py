n = int(input())
if n < 1 or n > 10_000:
    raise ValueError

result = 0
for i in range(1, n+1):
    result += i

print(result)
