# 약수들의 합

def solve(n: int):
    nums = list()
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)
    if n != sum(nums):
        print(f'{n} is NOT perfect.')
        return

    print(f'{n} = {" + ".join(list(map(str, nums)))}')


if __name__ == '__main__':
    while True:
        n = int(input())
        if n == -1:
            break
        solve(n)
