def sosu(num: int) -> [bool]:
    is_prime = [True] * (num + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False

    return is_prime


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    sosu_list = sosu(1000)

    result = 0
    for num in nums:
        if sosu_list[num]:
            result += 1

    print(result)
