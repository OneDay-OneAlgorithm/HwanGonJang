def solution(n, s):
    answer = []

    if n > s:
        return [-1]
    
    num = s // n
    rest = s % n

    for _ in range(n):
        answer.append(num)

    while rest:
        answer[rest] += 1
        rest -= 1

    answer.sort()
    return answer

n = 2
s = 9
print(solution(n, s))