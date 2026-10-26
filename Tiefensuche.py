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

def find_path(graph, node, end, visited=None):
    """Returns the list of adjacent nodes from 'node' to 'end' if it exists,
       returns False otherwise.
 
       If node is None, the first node in graph is chosen.
       If end is None, the last node in graph is chosen.
       If visited is not None, it contains the list of already visited nodes.
    """
    
    if visited == None:
        visited = set()
 
    # If node has already been visited, we closed a cycle - return false.
    if node in visited:
        return False
 
    # Local check: if node and end are the same, we have a trivial solution.    
    if node == end:
        return [end]
 
    # Record the current node as visited so that we break cycles should we return to it
    # in the recursion.
    visited.add(node)
 
    # Recursion: If we find a path p from any of our neighbors to end, there is
    # a path from 'node' to end that consists of [node] + p.
    edges = graph[node]
    for neighbor in edges:
        path = find_path(graph, neighbor, end, visited)
        if path:
            # We have found a path from neighbor to end
            # -> the path from node to end is the same path, with node prepended.
            return [node] + path
    # None of our neighbors has a path to 'end' -> give up.
    return False

print(find_path(graph, "ksr", "bahnhof"))