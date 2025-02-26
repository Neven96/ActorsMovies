from readactors import read_actors
from readmovies import read_movies
from actormovielisting import movie_magic
from buildgraph import buildgraph
from drawgraph import drawgraph
from shortestpath import shortest_path_from
from dfs import dfs

from collections import defaultdict
import time

def main():

    actors = read_actors()
    movies = read_movies()

    print('Creating the lists')
    start_time = time.perf_counter_ns()
    shared_movies, actor_names, movie_titles = movie_magic(actors, movies)
    time_used = time.perf_counter_ns() - start_time
    print('Full lists: ', time_used)

    print('\nBuilding the graph:')
    start_time = time.perf_counter_ns()
    # Builds the graph
    G = buildgraph(shared_movies)
    time_used = time.perf_counter_ns() - start_time
    print('Graph time: ', time_used)

    oppgave2 = True
    oppgave3 = True
    oppgave4 = False

    # The ids of the actors to check path
    actor_from = 'nm0942926'
    actor_to = 'nm7153679'

    print('\nAdding the shared actors together')
    start_time = time.perf_counter_ns()

    if oppgave2 or oppgave3:
        # Lists the actors and all they have acted with
        # Goes through the list with the both actors as key, to catch any that was missing

        co_stars_dict = defaultdict(list)
        for shared in shared_movies:
            actor1, actor2, _, movie_id = shared
            co_stars_dict[actor1].append([actor2, movie_id])
            co_stars_dict[actor2].append([actor1, movie_id])
        
        for actor_id, co_stars in co_stars_dict.items():
            actor_names[actor_id]['co_stars'] = co_stars

    time_used = time.perf_counter_ns() - start_time
    print('Co-star time: ', time_used)

    # Oppgave 2
    print('\nOppgave 2:')
    if oppgave2:
        # Uses the shortest path from algorithm to find the shortest path to all actors
        path, costs = shortest_path_from(G, actor_from)
        # print('Shortest path done', end='\r')

        full_path = [actor_to]
        target = actor_to

        # Maps all the actors in the path from actor_to to actor_from
        while target != actor_from:
            target = path[target]
            full_path.append(target)
        # Reverses the actors so that we go from actor_from to actor_to
        full_path = full_path[::-1]

        full_movie_path = []

        # Compares the actors with their co-stars to create a list over which movies they played in togheter to form a path with both actors and movies
        for i in range(len(full_path)):
            if i+1 == len(full_path):
                break
            for co_star in actor_names[full_path[i]]['co_stars']:
                if full_path[i+1] == co_star[0]:
                    full_movie_path.append(co_star)

        # Just a force fix, because sometimes it adds the actor that we're walking from instead of the one we're walking to
        for i in range(len(full_movie_path)):
            full_movie_path[i][0] = full_path[i+1]

        print(actor_names[actor_from]['name'])
        for stuff in full_movie_path:
            print(f'===[{movie_titles[stuff[1]]['title']} ({movie_titles[stuff[1]]['rating']})] ===> {actor_names[stuff[0]]['name']}')
    else:
        print('Set "oppgave2" to True to get the print')

    # Oppgave 3
    # This now works!!!
    print('\nOppgave 3:')
    if oppgave3:
        # Changes the weight of all movies, so that the best movies have lowest weight
        for i in range(len(shared_movies)):
            shared_movies[i][2] = str(10.0-float(shared_movies[i][2]))
        new_G = buildgraph(shared_movies)
        path, costs = shortest_path_from(new_G, actor_from)

        full_path = [actor_to]
        target = actor_to

        # Maps all the actors in the path from actor_to to actor_from
        while target != actor_from:
            target = path[target]
            full_path.append(target)
        # Reverses the actors so that we go from actor_from to actor_to
        full_path = full_path[::-1]

        full_movie_path = []

        # Compares the actors with their co-stars to create a list over which movies they played in togheter to form a path with both actors and movies
        for i in range(len(full_path)):
            if i+1 == len(full_path):
                break
            for co_star in actor_names[full_path[i]]['co_stars']:
                if full_path[i+1] == co_star[0]:
                    full_movie_path.append(co_star)

        # A fix for the too many movies stuff, but this stuff fixes it
        # NEW FIX START
        full_movie_path_dict = {}

        # Adds all the actors and their movies to a dict, because it grabs 1 actor, but many movies
        for actor_movie in full_movie_path:
            if actor_movie[0] in full_movie_path_dict:
                full_movie_path_dict[actor_movie[0]].append(actor_movie[1])
            else:
                full_movie_path_dict[actor_movie[0]] = [actor_movie[1]]

        full_movie_path_fixed = []

        # Compares each movie that I grabbed that the actors have shared and gives back the one with the highest rating
        for actor in full_movie_path_dict:
            best_movie = ''
            best_rating = 1.0
            for movies in full_movie_path_dict[actor]:
                if float(movie_titles[movies]['rating']) > float(best_rating):
                    best_movie = movies
                    best_rating = float(movie_titles[movies]['rating'])

            full_movie_path_fixed.append([actor, best_movie])

        # The best movie will always be the last movie, so could also just grab the last movie, but I chose to be more thorough
        # for actor in full_movie_path_dict:
        #     full_movie_path_fixed.append([actor, full_movie_path_dict[actor][-1]])

        # NEW FIX END

        # Just a force fix, because sometimes it adds the actor that we're walking from instead of the one we're walking to
        for i in range(len(full_movie_path_fixed)):
            full_movie_path_fixed[i][0] = full_path[i+1]


        print(actor_names[actor_from]['name'])
        for stuff in full_movie_path_fixed:
            print(f'===[{movie_titles[stuff[1]]['title']} ({movie_titles[stuff[1]]['rating']})] ===> {actor_names[stuff[0]]['name']}')
        print(f'Total weight: {costs[actor_to]}')

    else:
        print('Set "oppgave3" to True to get the print')

    # Oppgave 4
    print('\nOppgave 4:')

    if oppgave4:
        new_actor_names_dict = actor_names
        connections = {}

        # Use the depth first search to get the length of a component, then adds the times it received that length to a dict
        while len(new_actor_names_dict) > 0:
            conCom = dfs(G, list(new_actor_names_dict.keys())[0])
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
            print(f'There are {str(connection[1])} components of size {str(connection[0])}')

        # print('Unique connected components: ', conCom)
        # Since my program won't take the 1 length ones into the shared_movies dict, I know excatly how long it is

if __name__ == '__main__':
    full_progam_time = time.perf_counter_ns()
    main()
    full_time_used = time.perf_counter_ns() - full_progam_time
    print('Full program time: ', full_time_used)
