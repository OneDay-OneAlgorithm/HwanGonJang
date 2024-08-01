def solution(n, money):
    dp = [1] + [0] * n

    for coin in money:
        for price in range(coin, n + 1):
            dp[price] += dp[price - coin]  # price - coin 의 경우의 수에 coin을 더하는 것이기 때문에 경우의 수가 같다.

    return dp[-1] % 1000000007


n = 5
money = [1, 2, 5]
print(solution(n, money))