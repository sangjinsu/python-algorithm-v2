T = int(input())
nums = [list(map(int, input().split())) for _ in range(T)]
for i in range(T):
    result = nums[i][0] + nums[i][1]
    print(f'Case #{i + 1}: {result}')
