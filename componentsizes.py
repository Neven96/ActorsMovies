from dfs import dfs
from collections import Counter

def component_sizes(graph, actor_names):
    '''
    Finds the sizes of all the parts of the graph and counts them

    Parameters
    -----------
    graph : tuple
        The output from the buildgraph() function, with vertices, edges and weights
    actor_names : dict
        A dictionary with actor_ids as keys and names and co-stars as values
    '''

    remaining_actors = set(actor_names.keys())
    component_counts = Counter()

    # Using depth-first search to get the length of a component, then adds it to the count
    while remaining_actors:
        start_actor = next(iter(remaining_actors))

        connected_actors = dfs(graph, start_actor)
        component_size = len(connected_actors)

        component_counts[component_size] += 1

        remaining_actors -= connected_actors

    for size in sorted(component_counts.keys(), reverse=True):
        count = component_counts[size]
        print(f'There are {count} components of size {size}')
