from buildgraph import buildgraph
from shortestpath import shortest_path_from

def find_shortest_path_weighted(shared_movies, actor_names, movie_titles, actor_from, actor_to):
    '''
    Finds the shortest path between two actors based on co-stars, weighted for the best movie

    Parameters
    -----------
    shared_movies : list
        The list containing lists with actor pairs and their shared movie
    actor_names : dict
        The dictionary containing actor_ids as keys and names and co-stars as values
    movie_titles : dict
        The dictionary containing movie_ids as keys and title, rating and actors as values
    actor_from : str
        The string with the starting actor
    actor_to : str
        The string with the actor to path to
    '''

    # Changes the weight of all movies, so that the best movies have lowest weight
    weighted_shared_movies = [[item[0], item[1], str(10.0-float(item[2])), item[3]] for item in shared_movies]

    # Creates a new graph using the new weights
    new_graph = buildgraph(weighted_shared_movies)
    path, costs = shortest_path_from(new_graph, actor_from)

    full_path = []
    shared_movie_ids = []
    current = actor_to

    # Maps all the actors in the path from actor_to to actor_from
    while current != actor_from:
        full_path.append(current)
        current = path[current]
    full_path.append(actor_from)
    # Reverses the actors so that we go from actor_from to actor_to
    # It was somehow easier to get this to work than other way
    full_path.reverse()

    # Creating a dict for faster handling of each pair
    co_star_dict = {}
    for actor_id in full_path[:-1]:
        co_star_dict[actor_id] = {co_star[0]: co_star[1] for co_star in actor_names[actor_id]['co_stars']}

    full_movie_path_fixed = []
    for i in range(len(full_path) - 1):
        current_actor = full_path[i]
        next_actor = full_path[i+1]

        if next_actor in co_star_dict[current_actor]:
            shared_movie_ids = [co_star_dict[current_actor][next_actor]]
        else:
            shared_movie_ids = [co_star[1] for co_star in actor_names[current_actor]['co_stars'] if co_star[0] == next_actor]

        # Finds the best movie based on its rating
        best_movie = ''
        best_rating = 0.0

        for movie_id in shared_movie_ids:
            movie_rating = float(movie_titles[movie_id]['rating'])
            if movie_rating > best_rating:
                best_movie = movie_id
                best_rating = movie_rating

        if best_movie:
            full_movie_path_fixed.append([next_actor, best_movie])

    print(actor_names[actor_from]['name'])
    
    for actor_movie in full_movie_path_fixed:
        actor_id, movie_id = actor_movie
        movie_title = movie_titles[movie_id]['title']
        movie_rating = movie_titles[movie_id]['rating']
        actor_name = actor_names[actor_id]['name']
        print(f'===[{movie_title} ({movie_rating})] ===> {actor_name}')

    print(f'Total weight: {round(costs[actor_to], 1)}, the lower the better')
