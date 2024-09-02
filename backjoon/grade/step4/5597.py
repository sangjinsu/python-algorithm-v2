
result = [1] * 31
for _ in range(28):
    i = int(input())
    result[i] = 0

for i in range(1, 31):
    if result[i] > 0:
        print(i)
