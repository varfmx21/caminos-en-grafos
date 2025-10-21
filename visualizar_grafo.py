import matplotlib.pyplot as plt
import networkx as nx

# Importar la clase WeightedGraph
from grafos import WeightedGraph

def visualizar_grafo(grafo_personalizado, titulo="Grafo"):
    """
    Visualiza un grafo WeightedGraph usando matplotlib y networkx.
    
    param grafo_personalizado: Instancia de WeightedGraph
    param titulo: Título del grafo
    """
    # Crear grafo de networkx
    if grafo_personalizado._directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Agregar nodos
    for vertice in grafo_personalizado.vertices():
        G.add_node(vertice)
    
    # Agregar aristas con pesos
    for arista in grafo_personalizado.edges():
        G.add_edge(arista[0], arista[1], weight=arista[2])
    
    # Configurar visualización
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)  # Layout para posicionar los nodos
    
    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=1500, alpha=0.9)
    
    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, 
                          arrows=True, arrowsize=20, 
                          arrowstyle='->' if grafo_personalizado._directed else '-',
                          edge_color='gray')
    
    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    # Dibujar pesos de aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12)
    
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f'{titulo.replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear grafo no dirigido
    print("\nCreando grafo no dirigido...")
    gr_no_dirigido = WeightedGraph(directed=False)
    
    # Agregar vértices
    for i in range(1, 6):
        gr_no_dirigido.add_vertex(i)
    
    # Agregar aristas
    gr_no_dirigido.add_edge("", 2, 1)
    gr_no_dirigido.add_edge(1, 3, 1)
    gr_no_dirigido.add_edge(2, 3, 3)
    gr_no_dirigido.add_edge(3, 4, 4)
    gr_no_dirigido.add_edge(4, 5, 5)
    
    # Visualizar
    visualizar_grafo(gr_no_dirigido, "Grafo No Dirigido")
    
    print("\n¡Grafos generados exitosamente!")
