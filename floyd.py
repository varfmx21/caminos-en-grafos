#----------------------------------------------------------------------------------
# Example of implementation of the Floyd-Warshall Algorithm.
#----------------------------------------------------------------------------------
import numpy as np

#----------------------------------------------------------------------------------
# WeightedGraph class
#----------------------------------------------------------------------------------
class WeightedGraph:
    """
    Class that is used to represent a weighted graph. Internally, the class
    uses an adjacency matrix to store the vertices and edges of the graph. 
    This adjacency matrix is defined by a list of lists, whose elements indicate 
    the weights of the edges. A weight of 0 indicates that there is no connection
    between nodes.
    The graph can be directed or indirected. In the class constructor, this
    property is set. The behaviour of some operations depends on this property.
    This graph class assumes that it is not possible to have multiple links
    between vertices.
    """
    _directed = True  # This flag indicates whether the graph is directed or indirected.
    _vertices = []  # The list of vertices.
    _adjacency_matrix = []  # The adjacency matrix.

    def __init__(self, directed: bool = False):
        """
        This constructor initializes an empty graph.
        param directed: A flag that indicates whether the graph is directed
        (True) or undirected (False).
        """
        self._directed = directed
        self._vertices = []
        self._adjacency_matrix = []

    def vertices(self):
        """
        This method returns the list of vertices.
        """
        return self._vertices

    def add_vertex(self, v):
        """
        Add vertex to the graph.
        param v: The new vertex to be added to the graph.
        """
        if v in self._vertices:
            print("Warning: Vertex ", v, " already exists")
        else:
            self._vertices.append(v)
            n = len(self._vertices)
            if n > 1:
                for vertex in self._adjacency_matrix:
                    vertex.append(0)
            self._adjacency_matrix.append(n*[0])

    def add_edge(self, v1, v2, e=0):
        """
        Add edge to the graph. The edge is defined by two vertices v1 and v2,
        and the weight e of the edge.
        param v1: The start vertex of the new edge.
        param v2: The end vertex of the new edge.
        param e: The weight of the new edge.
        """
        if v1 not in self._vertices:
            # The start vertex does not exist.
            print("Warning: Vertex ", v1, " does not exist.")
        elif v2 not in self._vertices:
            # The end vertex does not exist.
            print("Warning: Vertex ", v2, " does not exist.")
        elif not self._directed and v1 == v2:
            # The graph is undirected, so it is no allowed to have autocycles.
            print("Warning: An undirected graph cannot have autocycles.")
        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = e
            if not self._directed:
                self._adjacency_matrix[index2][index1] = e

def floyd_warshall(M):
    n = len(M)
    INF = float('inf')
    
    # Inicializar: cambiar 0s por infinito excepto en la diagonal
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = 0
            elif M[i][j] == 0:
                M[i][j] = INF
    
    # Algoritmo Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][k] + M[k][j] < M[i][j]:
                    M[i][j] = M[i][k] + M[k][j]
    
    return M

# Create graph
gr = WeightedGraph(directed=False)
gr.add_vertex("Zrusall")
gr.add_vertex("Goxmont")
gr.add_vertex("Adaset")
gr.add_vertex("Ertonwell")
gr.add_vertex("Niaphia")
gr.add_vertex("Lagos")
gr.add_vertex("Duron")
gr.add_vertex("Blebus")
gr.add_vertex("Togend")
gr.add_vertex("Ontdale")
gr.add_vertex("Goding")
gr.add_vertex("Ylane")
gr.add_vertex("Strento")
gr.add_vertex("Oriaron")
gr.add_edge("Zrusall", "Goxmont", 112)
gr.add_edge("Zrusall", "Adaset", 15)
gr.add_edge("Zrusall", "Strento", 121)
gr.add_edge("Goxmont", "Adaset", 103)
gr.add_edge("Goxmont", "Niaphia", 212)
gr.add_edge("Adaset", "Ertonwell", 130)
gr.add_edge("Ertonwell", "Duron", 121)
gr.add_edge("Ertonwell", "Niaphia", 56)
gr.add_edge("Niaphia", "Lagos", 300)
gr.add_edge("Duron", "Lagos", 119)
gr.add_edge("Duron", "Blebus", 160)
gr.add_edge("Blebus", "Togend", 121)
gr.add_edge("Blebus", "Oriaron", 291)
gr.add_edge("Oriaron", "Strento", 221)
gr.add_edge("Oriaron", "Ylane", 117)
gr.add_edge("Oriaron", "Ontdale", 219)
gr.add_edge("Ontdale", "Ylane", 98)
gr.add_edge("Ontdale", "Goding", 88)
gr.add_edge("Ontdale", "Togend", 210)
gr.add_edge("Ontdale", "Blebus", 165)
gr.add_edge("Ylane", "Strento", 99)

print("=" * 60)
print("CAMINOS OPTIMOS DESDE GODING")
print("=" * 60)
matriz = floyd_warshall(gr._adjacency_matrix)

vertices = gr.vertices()
nodo_origen = "Goding"

# Encontrar el índice del nodo origen
if nodo_origen in vertices:
    indice_origen = vertices.index(nodo_origen)
        
    for j in range(len(vertices)):
        if j != indice_origen:
            destino = vertices[j]
            distancia = matriz[indice_origen][j]
            
            if distancia != float('inf'):
                print(f"{nodo_origen} -> {destino}: {int(distancia)}")
            else:
                print(f"{nodo_origen} -> {destino}: No hay camino")
else:
    print(f"Error: El nodo {nodo_origen} no existe en el grafo")

print("\n" + "=" * 60)

#----------------------------------------------------------------------------------
# End of file
#----------------------------------------------------------------------------------