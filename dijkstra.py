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


def build_path_from_parents(graph, parents, start, end):
    """Baut den Pfad vom Start- zum Endknoten mithilfe des parents-Dictionarys auf."""
    path = [end]
    while path[-1] != start:
        if path[-1] not in parents:
            return None  # Kein Pfad vorhanden
        path.append(parents[path[-1]])
    path.reverse()
    return path

def shortest_path(graph, start, end):
    
    candidates = PriorityQueue()
    candidates.put((0, start))
    parents = {}
    distances = {start: 0}
    
    while not candidates.empty():
        distance, node = candidates.get()
        
        if node == end:  # Wir sind am Ziel angekommen
            return build_path_from_parents(graph, parents, start, end)
            
        if distances.get(node, inf) < distance:
            continue  # Knoten wurde bereits über einen kürzeren Weg besucht
    
        for neighbor, edge in graph[node].items():
            new_distance = distance + edge
            old_distance = distances.get(neighbor, inf)
            
            if old_distance <= new_distance:
                continue  # Nachbar wurde bereits über einen kürzeren Weg entdeckt
                
            distances[neighbor] = new_distance
            candidates.put((new_distance, neighbor))
            parents[neighbor] = node
            
    return None  # Kein Pfad gefunden

    
    
ergebnis = shortest_path(graph, 'ksr', 'bahnhof')
print("Gefundener Pfad:", ergebnis)