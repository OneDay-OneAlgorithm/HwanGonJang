def solution(n, t, m, timetable):
    answer = ''

    shuttle_start = 540
    shuttle_time = []
    for i in range(n):
        shuttle_time.append(shuttle_start + (t * i))

    new_timetable = []
    for time in timetable:
        hour, minute = time.split(':')
        hour, minute = int(hour), int(minute)
        new_timetable.append(hour * 60 + minute)
    timetable = sorted(new_timetable)

    crew_idx = 0
    for shuttle in shuttle_time:
        crew_count = 0
        while crew_count < m and crew_idx < len(timetable) and timetable[crew_idx] <= shuttle:
            crew_idx += 1
            crew_count += 1

        if crew_count < m:
            answer = shuttle
        else:
            answer = timetable[crew_idx - 1] - 1

    return str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)


n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))