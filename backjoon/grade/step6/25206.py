import sys


def map_major_score(score: str) -> float:
    if score == 'A+':
        return 4.5
    if score == 'A0':
        return 4.0
    if score == 'B+':
        return 3.5
    if score == 'B0':
        return 3.0
    if score == 'C+':
        return 2.5
    if score == 'C0':
        return 2.0
    if score == 'D+':
        return 1.5
    if score == 'D0':
        return 1.0
    return 0.0


if __name__ == '__main__':
    T = 20
    score_list = [sys.stdin.readline().split() for _ in range(T)]
    score_list = list(filter(lambda score: score[2] != 'P', score_list))
    avg = (sum(map(lambda score: float(score[1]) * map_major_score(score[2]), score_list)) /
           sum(map(lambda score: float(score[1]), score_list)))
    print(avg)
