from collections import defaultdict

def co_star_search(shared_movies, actor_names):
    # Lists the actors and all they have acted with
    # Goes through the list with the both actors as key, to catch any that was missing
    co_stars_dict = defaultdict(list)
    for shared in shared_movies:
        actor1, actor2, _, movie_id = shared
        co_stars_dict[actor1].append([actor2, movie_id])
        co_stars_dict[actor2].append([actor1, movie_id])

    for actor_id, co_stars in co_stars_dict.items():
        actor_names[actor_id]['co_stars'] = co_stars

    return actor_names