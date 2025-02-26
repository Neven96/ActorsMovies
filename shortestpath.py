from collections import defaultdict
from heapq import heappush, heappop

def shortest_path_from(G, s):
    V, E, w = G
    Q = [(0, s)]
    D = defaultdict(lambda: float('inf'))
    parents = {s: None}
    D[s] = 0

    while Q:
        cost, v = heappop(Q)
        for u in E[v]:
            c = cost + w[(v, u)]
            if c < D[u]:
                D[u] = c
                heappush(Q, (c, u))
                parents[u] = v

    return parents, D
