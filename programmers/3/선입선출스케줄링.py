def solution(n, cores):

    if n <= len(cores):
        return n
    else:
        n -= len(cores)
        left = 1
        right = max(cores) * n

        while left < right:
            mid = (left + right) // 2
            capacity = 0
            for c in cores:
                capacity += mid // c
            if capacity >= n:
                right = mid  # right은 언제나 정답, mid는 마지막 단계에서 잘못된 값이 들어갈 수 있음
            else:
                left = mid + 1

            # print(left, mid, right, capacity)

        for c in cores:
            n -= (right-1) // c

        for i in range(len(cores)):
            if right % cores[i] == 0:
                n -= 1
                if n == 0:
                    return i + 1
                
n = 6
cores = [1, 2, 3]
print(solution(n, cores))