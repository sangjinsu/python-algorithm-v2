N, M = map(int, input().split())
result = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    result[i], result[j] = result[j], result[i]

print(*result)