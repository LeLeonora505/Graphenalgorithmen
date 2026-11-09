from math import inf
from queue import PriorityQueue

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


def shortest_path(graph, start, end):
    """Dijkstra shortest path."""
    # Candidates to process next, ordered by increasing distance.
    # The head of the queue is guaranteed to be the next node to be visited,
    # while the order of subsequent nodes could still be reordered if and preceding
    # node offers a shorter path to them.
    candidates = PriorityQueue()
    candidates.put((0, start))
    parents = {}
    # In addition to BFS, we record for each discovered node the currently known shortest
    # distance from start.
    distances = {start: 0}
    while candidates:
        print(distances)
        print(candidates.queue)
        input()
 
        # Let's visit the closest node not yet visited. The first candidate node is
        # guaranteed to be the closest one of the candidates.
        distance, node = candidates.get()
        if node == end:  # We're done.
            return build_path_from_parents(graph, parents, start, end)
        if distances.get(node, inf) < distance:
            continue  # Node was already visited. See comment below.
 
        for neighbor, edge in graph[node].items():
            new_distance = distance + edge
            old_distance = distances.get(neighbor, inf)
            if old_distance <= new_distance:
                continue  # Neighbor already discovered via some shorter path
            # Otherwise: we discovered a shorter (or new) path to neighbor - record it
            # and add to candidates.
            distances[neighbor] = new_distance
 
            # To be correct, we'd need to remove any old record (old_distance, neighbor) 
            # in the candidates, but that is expensive. Instead, we leave it in and
            # rely on the fact that the neighbor will be visited only once through the shortest
            # path.
            candidates.put((new_distance, neighbor))
            parents[neighbor] = node
    return None  # No path found

print (shortest_path(graph, "ksr", "bahnhof"))