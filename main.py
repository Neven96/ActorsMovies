from readactors import read_actors
from readmovies import read_movies
from actormovielisting import movie_magic
from costarsearch import co_star_search
from buildgraph import buildgraph
from findshortestpath import find_shortest_path
from findshortestpathweighted import find_shortest_path_weighted
from connectionsizes import connection_sizes

import time

def main():
    # Reading the files of actors and movies
    actors = read_actors()
    movies = read_movies()

    start_time = time.perf_counter_ns()

    print('Creating the lists')
    shared_movies, actor_names, movie_titles = movie_magic(actors, movies)

    time_used = time.perf_counter_ns() - start_time
    print('Full lists: ', time_used)

    start_time = time.perf_counter_ns()

    # Builds the graph
    print('\nBuilding the graph:')
    graph = buildgraph(shared_movies)

    time_used = time.perf_counter_ns() - start_time
    print('Graph time: ', time_used)

    shortest_path = False
    weighted_path = True
    depth_search = False

    # The ids of the actors to check path
    actor_from = 'nm0942926'
    actor_to = 'nm7153679'

    start_time = time.perf_counter_ns()

    print('\nAdding the shared actors together:')
    if shortest_path or weighted_path:
        actor_names = co_star_search(shared_movies, actor_names)

    time_used = time.perf_counter_ns() - start_time
    print('Co-star time: ', time_used)

    # The ids of the actors to check path
    # Most famous actors should be usable,
    # but newer or smaller actors might not be
    actor_from = 'nm0942926'
    actor_to = 'nm7153679'

    print('\nActors chosen:')
    try:
        print(f'From: {actor_names[actor_from]['name']}')
        print(f'To: {actor_names[actor_to]['name']}')
    except KeyError:
        print('Actor id not in file')
        exit(1)
    
    start_time = time.perf_counter_ns()

    # Shortest path between actors, unweighted
    print('\nShortest path between actors:')
    if shortest_path:
       find_shortest_path(graph, actor_names, movie_titles, actor_from, actor_to)
    else:
        print('Set "shortest_path" to True to get the print')

    time_used = time.perf_counter_ns() - start_time
    print('Shortest path: ', time_used)

    start_time = time.perf_counter_ns()

    # Shortest path between actors, weighed by movie score
    print('\nShortest path between actors, but weighted on movie score:')
    if weighted_path:
        find_shortest_path_weighted(shared_movies, actor_names, movie_titles, actor_from, actor_to)
    else:
        print('Set "weighted_path" to True to get the print')

    time_used = time.perf_counter_ns() - start_time
    print('Weighted path: ', time_used)

    start_time = time.perf_counter_ns()

    # Oppgave 4
    print('\nDepth first search for finding the sizes of the connections:')
    if depth_search:
        connection_sizes(graph, actor_names)

    time_used = time.perf_counter_ns() - start_time
    print('Depth-first search: ', time_used)

if __name__ == '__main__':
    full_progam_time = time.perf_counter_ns()
    main()
    full_time_used = time.perf_counter_ns() - full_progam_time
    print('Full program time: ', full_time_used)
