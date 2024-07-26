def solution(matrix_sizes):
    n = len(matrix_sizes)
    
    dp = [[0 for j in range(n)] for i in range(n)]
    for gap in range(1, n):
        for start in range(0, n - gap):
            end = start + gap

            candidates = []
            for middle in range(start, end):
                candidates.append(
                    dp[start][middle] + dp[middle + 1][end] + 
                    (matrix_sizes[start][0] * matrix_sizes[middle][1] * matrix_sizes[end][1]))
            
            dp[start][end] = min(candidates)

    return dp[0][-1]

matrix_sizes = [[5,3],[3,10],[10,6]]

print(solution(matrix_sizes))