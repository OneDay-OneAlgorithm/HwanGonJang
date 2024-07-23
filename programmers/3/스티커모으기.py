# dp[i] = max(dp[i-1], dp[i-2] + sticker[i])

def solution(sticker):
    n = len(sticker)

    if n == 1:
        return sticker.pop()

    dp1 = [0] + sticker[:-1]
    dp2 = [0] + sticker[1:]

    for i in range(2, n):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + dp1[i])

    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + dp2[i])

    return max(dp1[-1], dp2[-1])


sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))