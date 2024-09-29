def solve(start: int, end: int) -> (int, int):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    primes = [i for i in range(start, end + 1) if is_prime[i]]

    if len(primes) == 0:
        return -1, -1

    return sum(primes), primes[0]


if __name__ == '__main__':
    start = int(input())
    end = int(input())
    total, minimum = solve(start, end)
    if total == -1 and minimum == -1:
        print(-1)
        exit(0)

    print(total)
    print(minimum)
