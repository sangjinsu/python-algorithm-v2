if __name__ == '__main__':
    angles = [int(input()) for _ in range(3)]

    if sum(angles) != 180:
        print('Error')
        exit(0)

    if angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
        print('Equilateral')
        exit(0)
    if angles[0] != angles[1] and angles[0] != angles[2] and angles[1] != angles[2]:
        print('Scalene')
        exit(0)

    print('Isosceles')
