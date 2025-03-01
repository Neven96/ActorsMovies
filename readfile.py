import os

def read_file(filename):
    '''
    Reads a file and returns a list with all the lines

    Parameters
    -----------
    filename : str
        The filename to be read, not whole path, just name

    Returns
    -----------
    read_list : list
        A list of lists which contains one line from the file, aka one actor,
        for each internal list 
    '''

    read_list = []
    file_path = os.path.join('.', 'inputs', filename)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            entity = line.rstrip().split('\t')
            read_list.append(entity)

    return read_list
