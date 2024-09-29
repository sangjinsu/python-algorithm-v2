def prime_factors(n):
    factors = []

    # 2로 나누기
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 홀수 소수로 나누기
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # n이 1이 아니면 n은 소수
    if n > 1:
        factors.append(n)

    return factors


if __name__ == '__main__':
    n = int(input())
    factors = prime_factors(n)
    for factor in factors:
        print(factor)