score = int(input())

if score < 0 or score > 100:
    raise ValueError('시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
