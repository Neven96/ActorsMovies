from collections import defaultdict

def buildgraph(lines):
    vertices = set()
    edges = defaultdict(set)
    movie_weights = {}

    for line in lines:
        actor1, actor2, weight = line[0:3]

        # Add vertices
        vertices.add(actor1)
        vertices.add(actor2)

        # Add edges
        edges[actor1].add(actor2)
        edges[actor2].add(actor1)

        weigth_float = float(weight)
        movie_weights[(actor1, actor2)] = weigth_float
        movie_weights[(actor2, actor1)] = weigth_float

    return vertices, edges, movie_weights