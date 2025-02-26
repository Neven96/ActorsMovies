from collections import defaultdict

def buildgraph(lines):
    vertices = set()
    edges = defaultdict(set)
    movie_weights = {}

    for line in lines:
        v, u, weight = line[0:3]

        # Add vertices
        vertices.add(v)
        vertices.add(u)

        # Add edges
        edges[v].add(u)
        edges[u].add(v)

        weigth_float = float(weight)
        movie_weights[(v, u)] = weigth_float
        movie_weights[(u, v)] = weigth_float

    return vertices, edges, movie_weights