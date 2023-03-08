import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def init():
    N = int(input())
    graph = defaultdict(list)

    for _ in range(N-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return N,graph

def find_parent(graph,root):
    cur = root
    for next in graph[cur]:
        if not parent_list[next]:
            parent_list[next] = cur
            find_parent(graph,next)
    return

if __name__ == '__main__':
    N, graph = init()
    parent_list = [0]*(N+1)
    parent_list[1] = 1
    find_parent(graph,1)
    for x in parent_list[2:]:
        print(x)