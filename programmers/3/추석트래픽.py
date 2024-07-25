def solution(lines):
    answer = 0
    n = len(lines)

    times = []
    for line in lines:
        times.append(get_times(line))

    for i in range(n):
        count = 0
        for j in range(i, n):
            if times[i][1] + 1000 > times[j][0]:
                count += 1

        answer = max(count, answer)

    return answer

def get_times(line):
    time = line.split()
    hour, minute, second, millisecond = int(time[1][:2]), int(time[1][3:5]), int(time[1][6:8]), int(time[1][9:])
    duration = float(time[2][:-1]) * 1000 - 1

    end_time = (hour * 60 * 60 * 1000) + (minute * 60 * 1000) + (second * 1000) + millisecond
    start_time = end_time - duration

    return (start_time, end_time)

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))