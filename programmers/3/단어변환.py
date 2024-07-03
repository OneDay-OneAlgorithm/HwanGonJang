from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin, target, words):
    if target not in words:
        return 0
    
    n = len(begin)
    q = deque()
    q.append([begin, 0])

    while q:
        now, step = q.popleft()

        if now == target:
            return step

        for word in words:
            count = 0
            for i in range(n):
                if now[i] != word[i]:
                    count += 1

            if count == 1:
                q.append([word, step + 1])

    return 0

print(solution(begin, target, words))