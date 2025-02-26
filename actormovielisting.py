from itertools import combinations

def movie_magic(actors, movies):
    '''
    Connects the actors and movies together, and creates a list of shared movies for every actor

    Parameters
    -----------
    actors : list
        A list of lists containing each actors id, name and movies they have been in
    movies : list
        A list of lists containing each movies id, title and rating

    Returns
    -----------
    shared_movies : list
        A list of list with pairs of actors, the movie they both starred in and the movies rating
    actor_names : dict
        A dictionary containing an actors name and each co-star they have had
    movie_titles : dict
        A dictionary containing a movies title, rating and all actors in the movie
    '''
    shared_movies = []
    actor_names = {}
    movie_titles = {}

    # Creates the list of actors and unique actor names
    for actor in actors:
        actor_names[actor[0]] = {'name': actor[1], 'co_stars': []}

    # Creates the dict with the movie and rating, and blank actors
    for movie in movies:
        movie_titles[movie[0]] = {'title': movie[1], 'rating': movie[2], 'actors': []}

    # Adds the actors to the movie dict
    for actor in actors:
        for i in range(2, len(actor)):
            if actor[i] in movie_titles:
                movie_titles[actor[i]]['actors'].append(actor[0])

    # Really slow, about 2-3 seconds
    # Creates the shared movie list with all actors who shared a movie and the movie they worked on
    for movie_id, movie_data in movie_titles.items():
        actors_list = movie_data['actors']

        if len(actors_list) > 1:
            movie_rating = movie_data['rating']

            for actor1, actor2 in combinations(actors_list, 2):
                shared_movies.append([actor1, actor2, movie_rating, movie_id])
                    
    return shared_movies, actor_names, movie_titles
