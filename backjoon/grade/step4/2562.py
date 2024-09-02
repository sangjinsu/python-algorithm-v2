T = 9
nums = [int(input()) for _ in range(T)]
max_num = max(nums)

print(max_num)
print(nums.index(max_num) + 1)