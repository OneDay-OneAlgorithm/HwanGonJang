MAX = 1e9

def solution(sequence):
    answer = 0
    n = len(sequence)
    s1 = s2 = 0
    s1_min = s2_min = 0
    pulse = 1

    for i in range(n):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)

        answer = max(answer, s1 - s1_min, s2 - s2_min)

        s1_min = min(s1, s1_min)
        s2_min = min(s2, s2_min)

        pulse *= -1


    return answer


sequence = [2, 3, -6, 1, 3, -1, 2, 4]	
print(solution(sequence))