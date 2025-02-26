import os

def read_movies():
    '''
    Reads the file containing the movies and their IMDB score

    Returns
    -----------
    movies : list
        A list of lists with each internal list being its own movie
    '''

    movies = []
    file_path = os.path.join('.', 'inputs', 'movies.tsv')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie = line.rstrip().split('\t')
            movies.append(movie)

    return movies
