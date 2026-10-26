
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

def dfs(graph, node, visited):
    visited = visited or []
    if node in visited:                 # Wenn schon besucht, zurück gehen
        return node
    visited.append(node)                # Neuer Knoten besuchen
    for neighbor in graph[node]:        # Nachbarn durchgehen
        dfs(graph, neighbor, visited)   # Nachbarn mit eigener Funktion besuchen
    return visited                      # Alle besuchten zurückgeben

print(dfs(graph,"weitenzelgstr", None))
