import os

def read_actors():
    '''
    Reads the file containing the actors and the movies they have been in

    Returns
    -----------
    actors : list
        A list of lists which contains one line from the file, aka one actor,
        for each internal list 
    '''
    
    actors = []
    file_path = os.path.join('.', 'inputs', 'actors.tsv')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            actor = line.rstrip().split('\t')
            actors.append(actor)

    return actors
