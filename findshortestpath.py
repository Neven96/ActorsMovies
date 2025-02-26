from shortestpath import shortest_path_from

def find_shortest_path(graph, actor_names, movie_titles, actor_from, actor_to):
    # Uses the shortest path from algorithm to find the shortest path to all actors
    path, costs = shortest_path_from(graph, actor_from)
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
    for path in full_movie_path:
        print(f'===[{movie_titles[path[1]]['title']} ({movie_titles[path[1]]['rating']})] ===> {actor_names[path[0]]['name']}')
