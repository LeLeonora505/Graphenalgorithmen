
graph = {
    "ksr": {"turnhalle": 1, "weitenzelgstr": 1, "sek": 2},
    "turnhalle": {},
    "weitenzelgstr": {"bahnhofstr": 8},
    "sek": {"bahnhofstr": 3, "hafenstr": 5, "zelgstr": 7},
    "bahnhofstr": {"bahnhof": 7, "ksr": 4},
    "hafenstr": {"bahnhof": 4},
    "zelgstr": {"bahnhof": 5},
    "bahnhof": {},
}

def create_path(visited,start, end):
    ''' TODO: Create the list of nodes from start to end given visited'''
    print(visited)
    path = []
    while start != end:
        path.append(end)
        end = visited(end)
    path.append(start)
    return list(reversed(path))
    
    


def bfs (graph, start, end):
    candidates= [start] # bekannt, aber noch nicht besucht
    visited = {start: None} # besucht in der Bfs-Reihenfolge

    while candidates:
        next = candidates.pop (0) # pop next node to visit
        # neuer Knoten
        print (f'Vistited: {next}')
        visited.append (next)
        if next == end:
            print('found end')
            return create_path (visited, start, end)
        
        #add neighbours of next candidates
        for neighbour in graph[next]:
            if candidates not in visited:
                candidates.append(neighbour)
                # Record the firdt parent of neighbour to
                # later recover the parent chain of and 
                visited[neighbour] = next

    return visited

print (bfs(graph, "ksr"))