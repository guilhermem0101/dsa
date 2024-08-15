from Queue import Queue

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}

def bfs(graph, node):
    visited = []
    fila = Queue()

    visited.append(node)
    fila.enqueue(node)

    while fila.is_empty:
        
        s = fila.dequeue()
        # print(s, end = " ")

        for filho in graph[s]:
            print(graph[s])
            if filho not in visited:
                visited.append(filho)
                fila.enqueue(filho)
                #print(visited)
                
bfs(graph, 'A')


