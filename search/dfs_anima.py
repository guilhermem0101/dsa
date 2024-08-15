import matplotlib.pyplot as plt
import networkx as nx

# Definindo o grafo
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

# Função para criar um gráfico que representa a árvore
def draw_tree(graph, visited_nodes):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    labels = {node: node for node in G.nodes()}

    node_colors = ['lightblue' if node in visited_nodes else 'lightgray' for node in G.nodes()]

    nx.draw(G, pos, labels=labels, with_labels=True, node_color=node_colors)
    plt.show()

def dfs(graph, node, visited_nodes):
    visited_nodes.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited_nodes:
            dfs(graph, neighbor, visited_nodes)

    draw_tree(graph, visited_nodes)

visited_nodes = []
dfs(graph, 'A', visited_nodes)
