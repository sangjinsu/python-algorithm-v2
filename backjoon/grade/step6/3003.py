import sys

chess = [1, 1, 2, 2, 2, 8]
nums = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(len(nums)):
    result.append(chess[i] - nums[i])

print(*result)
