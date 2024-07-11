N = 5
number = 12

def solution(N, number):
    if N == number:
        return 1
    
    s_list = [ set() for _ in range(8)]

    for i,s in enumerate(s_list, start=1):
        s.add(int(str(N) * i))

    for i in range(8):
        for j in range(i):
            for op1 in s_list[i - j - 1]:
                for op2 in s_list[j]:
                    s_list[i].add(op1 + op2)
                    s_list[i].add(op1 - op2)
                    s_list[i].add(op1 * op2)
                    if op2 != 0:
                        s_list[i].add(op1 // op2)

        if number in s_list[i]:
            return i + 1

    return -1

print(solution(N, number))