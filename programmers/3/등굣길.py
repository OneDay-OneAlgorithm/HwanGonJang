# dp[i][j] = dp[i-1][j] + dp[i][j-1] (i, j > 0)

m = 4
n = 3
puddles = [[2, 2]]

def solution(m, n, puddles):
    answer = 0

    path = [[0] * (m + 1) for _ in range(n + 1)]
    path[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue

            # puddles 좌표 바꾸기
            if [j, i] in puddles:
                path[i][j] = 0
                continue
            else:
                path[i][j] = (path[i - 1][j] + path[i][j - 1]) % 1000000007

    return path[-1][-1]

print(solution(m, n, puddles))