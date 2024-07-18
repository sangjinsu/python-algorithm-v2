import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.reverse()

result = 0
for coin in coins:
    if K <= 0:
        break
    if K < coin:
        continue
    result += K // coin
    K = K % coin

sys.stdout.write(str(result))
