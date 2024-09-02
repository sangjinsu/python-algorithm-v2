N = int(input())
nums = list(map(int, input().split()))
M = max(nums)
nums = [num / M * 100 for num in nums]

print(sum(nums) / len(nums))
