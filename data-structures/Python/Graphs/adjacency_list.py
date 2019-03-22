class ListGraph(object):

    def __init__(self, graph_list=None, max_vertices=1024):
        if graph_list:
            self._graph_list = graph_list
            self.num_vertices = graph_list.num_vertices
            self.num_edges = graph_list.num_edges
        else:
            self._graph_list = [None] * max_vertices
            self.num_vertices = 0
            self.num_edges = 0

        self.max_vertices = max_vertices

    def add_vertex(self, vertex):
        self._graph_list[vertex] = []
        self.num_vertices += 1

    def add_edge(self, edge, directed=False):
        if len(edge) != 2:
            raise ValueError('Edge must be iterable that contains 2 vertices. Got {} instead.'.format(edge))

        vertex1, vertex2 = edge
        if self._graph_list[vertex1] is None:
            self.add_vertex(vertex1)
        if self._graph_list[vertex2] is None:
            self.add_vertex(vertex2)

        self._graph_list[vertex1].append(vertex2)
        self.num_edges += 1
        if directed or vertex1 == vertex2:
            return
        self._graph_list[vertex2].append(vertex1)
        self.num_edges += 1

    def make_edge(self, vertex1, vertex2, directed=False):
        if self._graph_list[vertex1] is None:
            raise ValueError('Vertex({}) not found in Graph:'.format(vertex1))
        if self._graph_list[vertex2] is None:
            raise ValueError('Vertex({}) not found in Graph:'.format(vertex2))

        self._graph_list[vertex1].append(vertex2)
        self.num_edges += 1
        if directed or vertex1 == vertex2:
            return
        self._graph_list[vertex2].append(vertex1)
        self.num_edges += 1

    def vertices(self):
        vertices = [None] * self.num_vertices
        count = 0
        for index, v in enumerate(self._graph_list):
            if v:
                vertices[count] = index
                count += 1
        return vertices

    def neighbours(self, vertex):
        return self._graph_list[vertex]

    def edges(self):
        edges = [None] * self.num_edges
        count = 0
        for i in range(len(self._graph_list)):
            neighbours = self._graph_list[i]
            if not neighbours:
                continue
            for v in neighbours:
                edges[count] = [i, v]
                count += 1
        return edges
