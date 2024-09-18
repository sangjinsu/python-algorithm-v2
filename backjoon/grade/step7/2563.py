mat = [[0] * 100 for _ in range(100)]
T = int(input())
for _ in range(T):
    y1, x1 = map(int, input().split())
    y2, x2 = y1 + 10, x1 + 10
    for i in range(y1, y2):
        for j in range(x1, x2):
            mat[i][j] = 1

result = 0
for i in range(100):
    for j in range(100):
        result += mat[i][j]

print(result)
