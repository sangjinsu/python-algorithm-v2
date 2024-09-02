nums = [int(input()) for _ in range(10)]
result = [0] * (max(nums) + 1)
for num in nums:
    idx = num % 42
    result[idx] = 1

print(sum(result))
