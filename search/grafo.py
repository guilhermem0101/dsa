import networkx as nx
import matplotlib.pyplot as plt

# Defina o grafo
graph = {
  'A': ['B', 'G'],
  'B': ['C', 'D', 'E'],
  'C': [],
  'D': [],
  'E': ['F'],
  'F': [],
  'G': ['H'],
  'H': ['I'],
  'I': [],
}

# Crie um objeto de grafo direcionado (pode ser não direcionado, dependendo do seu caso)
G = nx.DiGraph()

# Adicione nós e arestas ao grafo
for node, neighbors in graph.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Desenhe o grafo
pos = nx.spring_layout(G, seed=42)  # Define a posição dos nós
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_color="black")
plt.title("Grafo Representado Visualmente")
plt.show()


# for vertice, vizinhos in graph.items():
#     print(f'Chave: {vertice}, Valor: {vizinhos}')