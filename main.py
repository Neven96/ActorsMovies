from readactors import read_actors
from readmovies import read_movies
from actormovielisting import movie_magic
from costarsearch import co_star_search
from buildgraph import buildgraph
from findpath import find_shortest_path
from findpathweighted import find_shortest_path_weighted
from componentsizes import component_sizes
from timekeeper import timekeeper

def main():
    #
    # For testing, or if you want to only see certain things
    #
    shortest_path = True
    weighted_path = True
    depth_search = True

    # Reading the files of actors and movies
    actors = read_actors()
    movies = read_movies()

    # Processing the input from the files properly into mangable lists and dicts
    print('Creating the lists')
    shared_movies, actor_names, movie_titles = timekeeper('Full lists', lambda: movie_magic(actors, movies))

    # The ids of the actors to check path
    # Most famous actors should be usable,
    # but newer or smaller actors might not be
    actor_from = ''
    actor_to = ''

    print('\nActors chosen:')
    try:
        actor_from = input('Choose starting actor(format is nm#######, 7 digits): ')
        actor_names[actor_from]['name']
    except KeyError:
        print('Actor id not in file, using fallback')
        actor_from = 'nm0942926'
        # Backup actors were chosen on random
        # I can certainly not remember why...

    try:
        actor_to = input('Choose ending actor(format is nm#######, 7 digits): ')
        actor_names[actor_to]['name']
    except KeyError:
        print('Actor id not in file, using fallback')
        actor_to = 'nm7153679'

    print(f'From: {actor_names[actor_from]['name']}')
    print(f'To: {actor_names[actor_to]['name']}')

    # Builds the graph
    # Slow function, about 7-8 seconds
    print('\nBuilding the graph:')
    graph = timekeeper('Graph time', lambda: buildgraph(shared_movies))

    print('\nAdding the shared actors together:')
    if shortest_path or weighted_path:
        actor_names = timekeeper('Co-star time', lambda: co_star_search(shared_movies, actor_names))

    # Shortest path between actors, unweighted
    print('\nShortest path between actors:')
    if shortest_path:
        timekeeper('Shortest path', lambda: find_shortest_path(graph, actor_names, movie_titles, actor_from, actor_to))
    else:
        print('Set "shortest_path" to True to get the print')

    # Shortest path between actors, weighed by movie score
    print('\nShortest path between actors, but weighted on movie score:')
    if weighted_path:
        timekeeper('Weighted path', lambda: find_shortest_path_weighted(shared_movies, actor_names, movie_titles, actor_from, actor_to))
    else:
        print('Set "weighted_path" to True to get the print')

    # Setting up connec
    print('\nDepth first search for finding the sizes of the connections:')
    if depth_search:
        timekeeper('Depth-first search', lambda: component_sizes(graph, actor_names))

if __name__ == '__main__':
    timekeeper('Full program time', lambda: main())
