class MatrixGraph(object):
    """
    Graph doesn't validate values of vertices for sake of good speed.
    User of this class should check what is the value of MAX_VERTICES and act accordingly.
    """

    def __init__(self, graph_matrix=None, max_vertices=1024):
        if graph_matrix:
            self._graph_matrix = graph_matrix
            self.num_vertices = graph_matrix.num_vertices
            self.num_edges = graph_matrix.num_edges
        else:
            self._graph_matrix = [[-1] * max_vertices for _ in range(max_vertices)]
            self.num_vertices = 0
            self.num_edges = 0

        self.max_vertices = max_vertices

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
        self.num_edges += 1
        if directed or vertex1 == vertex2:
            return
        self._graph_matrix[vertex2][vertex1] = 1
        self.num_edges += 1

    def make_edge(self, vertex1, vertex2, directed=False):
        if self._graph_matrix[vertex1][vertex1] == -1:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex1))
        if self._graph_matrix[vertex2][vertex2] == -1:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex2))

        self._graph_matrix[vertex1][vertex2] = 1
        self.num_edges += 1
        if directed or vertex1 == vertex2:
            return
        self._graph_matrix[vertex2][vertex1] = 1
        self.num_edges += 1

    def vertices(self):
        vertices = [None] * self.num_vertices
        count = 0
        for v in range(self.max_vertices):
            if self._graph_matrix[v][v] > -1:
                vertices[count] = v
                count += 1
        return vertices

    def neighbours(self, vertex):
        neighbours = []
        for index, v in enumerate(self._graph_matrix[vertex]):
            if v > 0:
                neighbours.append(index)
        return neighbours

    def edges(self):
        edges = [None] * self.num_edges
        count = 0
        for row in range(len(self._graph_matrix)):
            for index, vertex in enumerate(self._graph_matrix[row]):
                if vertex > 0:
                    edges[count] = (row, index)
                    count += 1
        return edges

    def dfs(self, source, destination):
        visited = set()
        return self._dfs(source, destination, visited)

    def _dfs(self, source, destination, visited):
        if source == destination:
            return True

        visited.add(source)
        for v in self.neighbours(source):
            if v not in visited:
                found = self._dfs(v, destination, visited)
                if found:
                    return True
        return False


if __name__ == '__main__':
    import sys

    graph = MatrixGraph(max_vertices=126)
    for i in [1, 2, 3, 20, 39, 120]:
        graph.add_vertex(i)

    graph.make_edge(1, 2)
    graph.make_edge(2, 3)
    graph.make_edge(3, 20)
    graph.make_edge(20, 39)
    graph.make_edge(39, 120)

    print('GRAPH CONSTRUCTED')

    print('Vertices:', graph.vertices())
    print('Number of edges:', graph.num_vertices)
    print('Number of edges:', graph.num_edges)
    print('Edges:', graph.edges())
    print('Neighbours of vertex 2:', graph.neighbours(2))
    print('Size of the Graph:', sys.getsizeof(graph._graph_matrix))

    print('Depth first search of the path between 1 and 120:', graph.dfs(1, 120))
