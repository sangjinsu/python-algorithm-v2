N, M = map(int, input().split())
nums = [i for i in range(0, N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    nums = nums[:a] + list(reversed(nums[a:b + 1])) + nums[b + 1:]

print(*nums[1:])
