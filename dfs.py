def dfs(graph, s):
    '''
    Depth-first search
    '''
    _, edges, _ = graph
    visited = set()
    stack = [s]
    result = []

    while stack:
        actor_id = stack.pop()
        if actor_id in visited:
            continue
        result.append(actor_id)
        visited.add(actor_id)
        for u in edges[actor_id]:
            stack.append(u)

    return result
