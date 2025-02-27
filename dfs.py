def dfs(graph, start_actor):
    '''
    Depth-first search for finding the sizes of the components

    Parameters
    -----------
    graph : tuple
        The output from the buildgraph() function, with vertices, edges and weights
    start_actor : str
        The string with an actors id to use as starting node

    Returns
    -----------
    visited : set
        A set containing all actors that can be reached by starting actor
    '''

    _, edges, _ = graph
    visited = set()
    stack = [start_actor]

    while stack:
        actor_id = stack.pop()
        if actor_id in visited:
            continue

        visited.add(actor_id)
        for edge in edges[actor_id]:
            stack.append(edge)

    return visited
