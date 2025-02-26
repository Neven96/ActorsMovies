from collections import defaultdict

def buildgraph(lines):
    V = set()
    E = defaultdict(set)
    w = dict()

    for line in lines:
        v, u, weight = line[0:3]

        V.add(v)
        V.add(u)

        E[v].add(u)
        E[u].add(v)

        w[(v, u)] = float(weight)
        w[(u, v)] = float(weight)

    return V, E, w