import sys
from collections import deque
input = sys.stdin.readline

def init():
    N = int(input())
    graph = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(N-1):
        a,b = map(int,input().split())
        graph[a][b] = graph[b][a] = 1
    return N,graph

def bfs(graph,root):
    q = deque([root])
    visited = [False]*(N+1)
    root_list = [0]*(N+1)

    while q:
        cur = q.popleft()
        for i in range(1,N+1):
            if graph[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = True
                root_list[i] = cur

    return root_list

if __name__ == '__main__':
    N, graph = init()
    root_list = bfs(graph,1)
    for x in root_list:
        print(x)