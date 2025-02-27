from collections import defaultdict

def co_star_search(shared_movies, actor_names):
    '''
    Lists the actors and all their co-stars

    Parameters
    -----------
    shared_movies : list
        A list containing lists of all the actor pairs and their connected movies
    actor_names : dict
        A dictionary containing actor_ids as keys and their names and empty list of co-stars as values

    Returns
    -----------
    actor_names : dict
        The same as the input, but with a full list of co-stars for each actor
    '''

    co_stars_dict = defaultdict(list)
    for shared in shared_movies:
        actor1, actor2, _, movie_id = shared
        co_stars_dict[actor1].append([actor2, movie_id])
        co_stars_dict[actor2].append([actor1, movie_id])

    for actor_id, co_stars in co_stars_dict.items():
        actor_names[actor_id]['co_stars'] = co_stars

    return actor_names