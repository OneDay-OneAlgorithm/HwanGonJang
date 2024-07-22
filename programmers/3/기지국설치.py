def solution(n, stations, w):
    answer = 0
    range = 2 * w + 1

    start = 1
    for station in stations:
        if station - w - start > 0:
            answer += (station - w - start) // range
            if (station - w - start) % range: answer += 1
        start = station + w + 1

    if n - start + 1 > 0:
        answer += (n - start + 1) // range
        if (n - start + 1) % range: answer += 1

    return answer

n = 11
stations = [4, 11]
w = 1

print(solution(n, stations, w))