from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    answer = 0

    # 3. DFS 풀이
    visited = [0] * n
    def dfs(node):
        visited[node] = 1
        for i in range(n):
            if not visited[i] and i != node and computers[i][node]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    # 2. BFS 풀이
    # visited = [0] * n
    # def bfs(node):
    #     q = deque([node])

    #     while q:
    #         node = q.popleft()
    #         visited[node] = 1
            
    #         for i in range(n):
    #             if not visited[i] and i != node and computers[i][node]:
    #                 q.append(i)

    # for i in range(n):
    #     if not visited[i]:
    #         bfs(i)
    #         answer += 1

    
    return answer

print(solution(n, computers))