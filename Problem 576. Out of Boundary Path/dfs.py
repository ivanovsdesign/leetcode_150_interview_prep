def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for adjacent in graph[node]:
            dfs(visited, graph, adjacent)
    
    return visited

def bfs(visited_bfs, graph, node):
    queue.append(node)
    visited_bfs.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for adjacent in graph[m]:
            if adjacent not in visited_bfs:
                visited_bfs.append(adjacent)
                queue.append(adjacent)


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set()
visited_bfs = []

queue = []

#print(dfs(visited, graph, '5'))
bfs(visited_bfs, graph, '5')