
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


def bfs (graph, start):
    candidates= [start] # bekannt, aber noch nicht besucht
    visited = [] # besucht in der Bfs-Reihenfolge

    while candidates:
        next = candidates.pop (0) # pop next node to visit
        if next in visited:
            continue
        # neuer Knoten
        print (f'Vistited: {next}')
        visited.append (next)

        #add neighbours of next candidates
        candidates.extend(graph[next].keys())
        print (f'Candidates: {candidates}')
    return visited

print (bfs(graph, "ksr"))