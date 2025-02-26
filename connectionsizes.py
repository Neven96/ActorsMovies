from dfs import dfs

def connection_sizes(graph, actor_names):
    new_actor_names_dict = actor_names
    connections = {}

    # Use the depth first search to get the length of a component, then adds the times it received that length to a dict
    while len(new_actor_names_dict) > 0:
        conCom = dfs(graph, list(new_actor_names_dict.keys())[0])
        if str(len(conCom)) in connections:
            connections[str(len(conCom))] = connections[str(len(conCom))]+1
        else:
            connections[str(len(conCom))] = 1

        for con in conCom:
            new_actor_names_dict.pop(con)

    # To sort the numbers I have to convert to int, but the dict I use takes str as keys, so I have to convert them back
    # It's way to late to figure out a better way for this, but the length of these are so small it doesn't really matter for big O
    connections_keys = list(connections.keys())
    connections_keys = [int(i) for i in connections_keys]
    connections_keys.sort()
    connections_keys = [str(i) for i in connections_keys]

    new_connections = []
    for key in connections_keys:
        new_connections.append([key, connections[key]])

    for connection in reversed(new_connections):
        print(
            f'There are {str(connection[1])} components of size {str(connection[0])}')

    # print('Unique connected components: ', conCom)
    # Since my program won't take the 1 length ones into the shared_movies dict, I know excatly how long it is
