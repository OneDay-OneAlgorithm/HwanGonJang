import heapq

def solution(n, works):
    if n >= sum(works):
        return 0

    works = [-w for w in works]
    heapq.heapify(works)

    for _ in range(n):
        w = heapq.heappop(works)
        w += 1
        heapq.heappush(works, w)

    return sum([w ** 2 for w in works])


n = 4
works = [4, 3, 3]

print(solution(n, works))