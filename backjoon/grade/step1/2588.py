num1 = int(input())
num2 = input()

nums = list(map(int, list(num2)))
nums.reverse()

for num in nums:
    print(num1 * num)

print(num1 * int(num2))
