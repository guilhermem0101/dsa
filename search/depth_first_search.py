from Stack import Stack

graph = {
  'A' : ['B','G'],
  'B' : ['C', 'D', 'E'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : ['H'],
  'H' : ['I'],
  'I' : [],
}

def dfs(graph, node):
  visited = []
  pilha = Stack()

  visited.append(node)
  pilha.push(node) 

  while pilha.is_empty:
    
    s = pilha.pop()    
    print(s, end = " ")
    
    for filho in reversed(graph[s]):
      print(graph[s])
      if filho not in visited:
        visited.append(filho)
        pilha.push(filho)

              

dfs(graph, 'A')


