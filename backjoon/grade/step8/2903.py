N = int(input())

k = 3
for i in range(2, N + 1):
    k = k * 2 - 1

print(k ** 2)
