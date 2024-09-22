def get_change(money: int) -> list[int]:
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    result = list()
    for coin in [quarter, dime, nickel, penny]:
        cnt, money = divmod(money, coin)
        result.append(cnt)

    return result


if __name__ == '__main__':
    T = int(input())
    money_list = [int(input()) for _ in range(T)]
    for money in money_list:
        print(*get_change(money))
