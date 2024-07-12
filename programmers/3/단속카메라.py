from collections import deque

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	

# 내 답안: 경로가 겹치는 자동차 수 일일히 세기
def solution(routes):
    answer = 0

    routes = sorted(routes, key=lambda x: x[0])

    q = deque(routes)
    temp = []
    start, end = q.popleft()
    while q:
        next_start, next_end = q.popleft()

        if start <= next_start <= end:
            start = next_start
            if next_end <= end:
                end = next_end
        else:
            answer += 1
            start, end = next_start, next_end

        if not q:
            answer += 1

    return answer

# 모범 답안: 자동차의 진출 위치를 기준으로 카메라 설치 후 비교
def solution2(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    cnt = 0

    for route in routes:
        if route[0] > camera:
            cnt += 1
            camera = route[1]

    return cnt

print(solution2(routes))