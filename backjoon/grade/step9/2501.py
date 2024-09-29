def solve(num: int, num2: int) -> int:
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    if len(result) >= num2:
        return result[num2 - 1]
    return 0


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solve(n, k))
