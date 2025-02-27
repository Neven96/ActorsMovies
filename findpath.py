from shortestpath import shortest_path_from

def find_shortest_path(graph, actor_names, movie_titles, actor_from, actor_to):
    '''
    Finds the shortest path between two actors based on co-stars, 
    kind of weighted after the worst movie

    Parameters
    -----------
    graph : tuple
        The output from the buildgraph() function, with vertices, edges and weights
    actor_names : dict
        The dictionary containing actor_ids as keys and names and co-stars as values
    movie_titles : dict
        The dictionary containing movie_ids as keys and title, rating and actors as values
    actor_from : str
        The string with the starting actor
    actor_to : str
        The string with the actor to path to
    '''

    # Uses the shortest path from algorithm to find the shortest path to all actors
    path, costs = shortest_path_from(graph, actor_from)

    full_path = []
    current = actor_to
    co_star_dict = {}

    # Maps all the actors in the path from actor_to to actor_from
    while current != actor_from:
        full_path.append(current)
        current = path[current]
    full_path.append(actor_from)
    # Reverses the actors so that we go from actor_from to actor_to
    # It was somehow easier to get this to work than other way
    full_path.reverse()

    for i in range(len(full_path) - 1):
        actor_id = full_path[i]
        co_star_dict[actor_id] = {co_star[0]: co_star[1] for co_star in actor_names[actor_id]['co_stars']}

    full_movie_path = []

    # Compares the actors with their co-stars to create a list over which movies they played in togheter to form a path with both actors and movies
    for i in range(len(full_path) - 1):
        current_actor = full_path[i]
        next_actor = full_path[i+1]

        if next_actor in co_star_dict[current_actor]:
            movie_id = co_star_dict[current_actor][next_actor]
            full_movie_path.append([next_actor, movie_id])

    print(actor_names[actor_from]['name'])

    for path in full_movie_path:
        actor_id, movie_id = path
        movie_title = movie_titles[movie_id]['title']
        movie_rating = movie_titles[movie_id]['rating']
        actor_name = actor_names[actor_id]['name']
        print(f'===[{movie_title} ({movie_rating})] ===> {actor_name}')
        
    print(f'Total weight: {round(costs[actor_to], 1)}, the lower the better')
