from collections import defaultdict

def buildgraph(lines):
    '''
    Builds a network of actors connected by shared movies

    Parameters
    -----------
    lines : list
        The shared_movies list which contains lists of actors and their connecting movies

    Returns
    -----------
    vertices : set
        A set of all the actors ids
    edges : defaultdict
        A dictionary with all the actors as keys and their shared actors as values
    movie_weights : dict
        A dictionary with the actors as tuple pairs of keys and the rating of the movie as values
        Used for setting up the distance between actors
    '''
    
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

        # Adds weights
        weight_float = float(weight)
        movie_weights[(actor1, actor2)] = weight_float
        movie_weights[(actor2, actor1)] = weight_float

    return vertices, edges, movie_weights