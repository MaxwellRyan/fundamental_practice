# a simple bfs implementation
def bfs(graph, node):
    visited = []
    queue = []
    order = []
    visited.append(node)
    queue.append(node)

    while queue:
        v = queue.pop(0)
        order.append(v)
        neighbors = graph[v]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return order
    
def main():
    graph = {
        5: [3, 7],
        3: [2, 4],
        7: [8],
        2: [],
        4: [8],
        8: []
    }

    order = bfs(graph, 5)
    print(order)

if __name__ == '__main__':
    main()