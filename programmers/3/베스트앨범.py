from collections import defaultdict

def solution(genres, plays):
    answer = []

    playlist = defaultdict(list)
    play_counts = defaultdict(int)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        playlist[genre].append((i, play))
        play_counts[genre] += play 

    # dictionary의 .items()는 [(k, v), ...] 형식으로 출력된다.
    for genre, count in sorted(play_counts.items(), key = lambda x: x[1], reverse = True):
        for i, play in sorted(playlist[genre], key = lambda x: x[1], reverse = True)[:2]:
            answer.append(i)

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))