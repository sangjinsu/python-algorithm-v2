N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(M)]

result = [0] * (N+1)
for row in mat:
    start, end, value = row
    for i in range(start, end+1):
        result[i] = value


print(*result[1:])