def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for vertex in graph[node]:
            dfs(visited, graph, vertex)

def main():
    graph = {
        'A': ['B','C'],
        'B': ['D','E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited = set()
    dfs(visited, graph, 'A')

if __name__ == '__main__':
    main()