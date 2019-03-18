class MatrixGraph(object):
    """
    Graph doesn't validate values of vertices for sake of good speed.
    User of this class should check what is the value of MAX_VERTICES and act accordingly.
    """

    def __init__(self, graph_matrix=None, max_vertices=1024):
        if graph_matrix:
            self._graph_matrix = graph_matrix
        else:
            self._graph_matrix = [[-1] * max_vertices for _ in range(max_vertices)]

        self.max_vertices = max_vertices
        self.num_vertices = 0

    def add_vertex(self, vertex):
        self._graph_matrix[vertex][vertex] = 0
        self.num_vertices += 1

    def add_edge(self, edge, directed=False):
        if len(edge) != 2:
            raise ValueError('Edge must be iterable that contains 2 vertices. Got {} instead.'.format(edge))

        vertex1, vertex2 = edge
        # check if vertices exist, if not create them.
        if self._graph_matrix[vertex1][vertex1] == -1:
            self.add_vertex(vertex1)
        if self._graph_matrix[vertex2][vertex2] == -1:
            self.add_vertex(vertex2)

        # Add edge
        self._graph_matrix[vertex1][vertex2] = 1
        if directed or vertex1 == vertex2:
            return
        self._graph_matrix[vertex2][vertex1] = 1

    def make_edge(self, vertex1, vertex2, directed=False):
        if self._graph_matrix[vertex1][vertex1] == -1:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex1))
        if self._graph_matrix[vertex2][vertex2] == -1:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex2))

        self._graph_matrix[vertex1][vertex2] = 1
        if directed or vertex1 == vertex2:
            return
        self._graph_matrix[vertex2][vertex2] = 1

    def vertices(self):
        vertices = [None] * self.num_vertices
        count = 0
        for v in range(self.max_vertices):
            if self._graph_matrix[v][v] > -1:
                vertices[count] = v
                count += 1
        return vertices


