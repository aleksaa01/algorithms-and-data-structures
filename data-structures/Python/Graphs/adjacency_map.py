# class EdgeNode(object):
#
#     def __init__(self, value):
#         self.value = value
#         self.adjacent_nodes = []
#
#
# class Graph(object):
#
#     MAX_VERTICES = 1000
#
#     def __init__(self):
#         self.edges = [None] * self.MAX_VERTICES
#         self.degree = [0] * self.MAX_VERTICES
#         self.num_vertices = 0
#         self.num_edges = 0
#         self.is_directed = False
#
#     def const


class Graph(object):

    def __init__(self, graph_dict=None):
        self._graph_dict = graph_dict if graph_dict else {}
        self.num_edges = graph_dict.num_edges if graph_dict else 0

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge, directed=False):
        """Creates both vertices if necessary and makes an edge."""
        if len(edge) != 2:
            raise ValueError('Edge must be iterable that contains 2 vertices. Got {} instead.'.format(edge))

        vertex1, vertex2 = edge
        if vertex1 not in self._graph_dict:
            self._graph_dict[vertex1] = [vertex2]
        else:
            self._graph_dict[vertex1].append(vertex2)
        self.num_edges += 1

        if directed:
            return

        if vertex2 not in self._graph_dict:
            self._graph_dict[vertex2] = [vertex1]
        else:
            self._graph_dict[vertex2].append(vertex1)
        self.num_edges += 1

    def make_edge(self, vertex1, vertex2, directed=False):
        try:
            self._graph_dict[vertex1].append(vertex2)
            self.num_edges += 1
        except KeyError:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex1))

        if directed or vertex1 == vertex2:
            return

        try:
            self._graph_dict[vertex2].append(vertex1)
            self.num_edges += 1
        except KeyError:
            # remove vertex2 from vertex1, because vertex2 doesn't exist.
            self._graph_dict[vertex1].pop()
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex1))

    def vertices(self):
        return list(self._graph_dict.keys())

    def edges(self):
        edges = [None] * self.num_edges
        count = 0
        for node in self._graph_dict:
            for neighbour in self._graph_dict[node]:
                edges[count] = (node, neighbour)
                count += 1
        return edges


if __name__ == '__main__':
    graph = Graph()
    for i in 'abcdef':
        graph.add_vertex(i)
    graph.make_edge('a', 'd')
    graph.make_edge('d', 'c')
    graph.make_edge('c', 'c')
    graph.make_edge('c', 'b')
    graph.make_edge('c', 'e')

    print('GRAPH CONSTRUCTED')

    print('Vertices:', graph.vertices())
    print('Graph:', graph._graph_dict)
    print('Number of edges:', graph.num_edges)
    print('Edges:', graph.edges())
