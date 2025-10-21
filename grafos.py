#----------------------------------------------------------------------------------
# Example a weighted graph class based on the adjacency list.
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
# WeightedGraph class
#----------------------------------------------------------------------------------
class WeightedGraph:
	"""
	Class that is used to represent a weighted graph. Internally, the class
	uses an adjacency list to store the vertices and edges of the graph. This adjacency list is defined by a
	dictionary, whose keys represent the vertices. For each vertex, there is a list of tuples (v,e)
	that indicate which vertices are connected to the vertex and their corresponding weights.
	The graph can be directed or indirected. In the class constructor, this property is set. The
	behaviour of some operations depends on this property.
	This graph class assumes that it is possible to have multiple links between vertices with different weights.
	"""
	_directed = True # This flag indicates whether the graph is directed or indirected.
	_adjacency_list = {} # The adjacency list of the graph.

	def __init__(self, directed: bool = False):
		"""
		This constructor initializes an empty graph.
		param directed: A flag that indicates whether the graph is directed (True) or undirected (False).
		"""
		self._directed = directed
		self._adjacency_list = {}

	def clear(self):
		"""
		This method clears the graph.
		"""
		self._adjacency_list = {}

	def number_of_vertices(self):
		"""
		This method returns the number of vertices of the graph.
		"""
		return len(self._adjacency_list)

	def vertices(self):
		"""
		This method returns the list of vertices.
		"""
		v = []
		for vi in self._adjacency_list:
			v.append(vi)
		return v

	def edges(self):
		"""
		This method returns the list of edges.
		"""
		e = []
		if self._directed:
			for v in self._adjacency_list:
				for edge in self._adjacency_list[v]:
					e.append((v, edge[0], edge[1]))
		else:
			for v in self._adjacency_list:
				for edge in self._adjacency_list[v]:
					if (edge[0], v, edge[1]) not in e:
						e.append((v, edge[0], edge[1]))
		return e

	def add_vertex(self, v):
		"""
		Add vertex to the graph.
		param v: The new vertex to be added to the graph.
		"""
		if v in self._adjacency_list:
			print("Warning: Vertex ", v, " already exists.")
		else:
			self._adjacency_list[v] = []

	def remove_vertex(self, v):
		"""
		Remove vertex from the graph.
		param v: The vertex to be removed from the graph.
		"""
		if v not in self._adjacency_list:
			print("Warning: Vertex ", v, " is not in graph.")
		else:
			# Remove vertex from adjacency list.
			self._adjacency_list.pop(v)
			# Remove edges where the vertex is an end point.
			for vertex in self._adjacency_list:
				self._adjacency_list[vertex] = [edge for edge in self._adjacency_list[vertex] if edge[0] != v]

	def add_edge(self, v1, v2, e=0):
		"""
		Add edge to the graph. The edge is defined by two vertices v1 and v2, and the weight e of the edge.
		param v1: The start vertex of the new edge.
		param v2: The end vertex of the new edge.
		param e: The weight of the new edge.
		"""
		if v1 not in self._adjacency_list:
			# The start vertex does not exist.
			print("Warning: Vertex ", v1, " does not exist.")
		elif v2 not in self._adjacency_list:
			# The end vertex does not exist.
			print("Warning: Vertex ", v2, " does not exist.")
		elif not self._directed and v1 == v2:
			# The graph is undirected, so it is not allowed to have autocycles.
			print("Warning: An undirected graph cannot have autocycles.")
		elif (v2, e) in self._adjacency_list[v1]:
			# The edge is already in graph.
			print("Warning: The edge (", v1, "," ,v2, ",", e, ") already exists.")
		else:
			self._adjacency_list[v1].append((v2, e))
			if not self._directed:
				self._adjacency_list[v2].append((v1, e))

	def remove_edge(self, v1, v2, e):
		"""
		Remove edge from the graph.
		param v1: The start vertex of the edge to be removed.
		param v2: The end vertex of the edge to be removed.
		param e: The weight of the edge to be removed.
		"""
		if v1 not in self._adjacency_list:
			# v1 is not a vertex of the graph
			print("Warning: Vertex ", v1, " does not exist.")
		elif v2 not in self._adjacency_list:
			# v2 is not a vertex of the graph
			print("Warning: Vertex ", v2, " does not exist.")
		else:
			self._adjacency_list[v1] = [edge for edge in self._adjacency_list[v1] if edge != (v2, e)]
			if not self._directed:
				self._adjacency_list[v2] = [edge for edge in self._adjacency_list[v2] if edge != (v1, e)]

	def adjacent_vertices(self, v):
		"""
		Adjacent vertices of a vertex.
		param v: The vertex whose adjacent vertices are to be returned.
		return: The list of adjacent vertices of v.
		"""
		if v not in self._adjacency_list:
			# The vertex is not in the graph.
			print("Warning: Vertex ", v, " does not exist.")
			return []
		else:
			return self._adjacency_list[v]

	def is_adjacent(self, v1, v2) -> bool:
		"""
		This method indicates whether vertex v2 is adjacent to vertex v1.
		param v1: The start vertex of the relation to test.
		param v2: The end vertex of the relation to test.
		return: True if v2 is adjacent to v1, False otherwise.
		"""
		if v1 not in self._adjacency_list:
			# v1 is not a vertex of the graph
			print("Warning: Vertex ", v1, " does not exist.")
			return False
		elif v2 not in self._adjacency_list:
			# v2 is not a vertex of the graph
			print("Warning: Vertex ", v2, " does not exist.")
			return False
		else:
			for edge in self._adjacency_list[v1]:
				if edge[0] == v2:
					return True
			return False

	def print_graph(self):
		"""
		This method shows the edges of the graph.
		"""
		for vertex in self._adjacency_list:
			for edges in self._adjacency_list[vertex]:
				print(vertex, " -> ", edges[0], " edge weight: ", edges[1])