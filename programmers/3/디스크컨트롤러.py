import heapq

def solution(jobs):
    answer = 0
    now = 0
    i = 0
    start = -1
    heap = []
    
    while i < len(jobs):
        print('hi')
        for job in jobs:
            if start < job[0] <= now:
                print(start, now, job[0], job[1])
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]	
print(solution(jobs))