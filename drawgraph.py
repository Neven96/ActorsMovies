def drawgraph(G):
    V, E, w = G
    seen_edges = set()

    for v in V:

        for u in E[v]:
            if (u, v) in seen_edges:
                continue
            seen_edges.add((v, u))

    return V, seen_edges
