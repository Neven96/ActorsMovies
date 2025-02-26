def dfs(G, s):
    '''
    Depth-first search
    '''
    _, E, _ = G
    visited = set()
    stack = [s]
    result = []

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        result.append(v)
        visited.add(v)
        for u in E[v]:
            stack.append(u)

    return result
