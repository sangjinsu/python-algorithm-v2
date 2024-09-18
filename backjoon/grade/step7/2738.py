if __name__ == '__main__':
    n, m = map(int, input().split())
    A = []
    B = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    for i in range(n):
        B.append(list(map(int, input().split())))

    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i].append(A[i][j] + B[i][j])

    for i in range(n):
        print(*result[i])
