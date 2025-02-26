from collections import defaultdict
from heapq import heappush, heappop

def shortest_path_from(graph, actor_id):
    '''
    Using Djikstra's algorithm for finding the shortest path between vertices

    Parameters
    -----------
    graph : list
        A list containing vertices, edges and weights for each movie
        The weights are based on movie score
    actor_id : str
        The string containing the id for the actor we chose as starting position

    Returns
    -----------
    parents : dict
        The path from one actor to another, through actor ids
    distances : defaultdict
        The score of each movie that connects the actors
    '''
    _, edges, weights = graph
    queue = [(0, actor_id)]
    distances = defaultdict(lambda: float('inf'))
    parents = {actor_id: None}
    distances[actor_id] = 0

    while queue:
        cost, current_vertex = heappop(queue)
        for neighbor in edges[current_vertex]:
            new_distance = cost + weights[(current_vertex, neighbor)]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(queue, (new_distance, neighbor))
                parents[neighbor] = current_vertex

    return parents, distances
