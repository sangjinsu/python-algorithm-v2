T = int(input().strip())
nums = [tuple(map(int, input().strip().split())) for _ in range(T)]

for num in nums:
    print(num[0] + num[1])
