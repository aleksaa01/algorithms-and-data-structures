from queue import Queue


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

    def dfs(self, source, destination):
        visited = set()
        return self._dfs(source, destination, visited)

    def _dfs(self, source, destination, visited):
        if source == destination:
            return True

        visited.add(source)
        for v in self.neighbours(source):
            if v in visited:
                continue
            res = self._dfs(v, destination, visited)
            if res:
                return True
        return False

    def bfs(self, source, destination):
        queue = Queue()
        visited = set()

        queue.put(source)
        visited.add(source)
        while not queue.empty():
            for v in self.neighbours(queue.get()):
                if v == destination:
                    return True
                elif v not in visited:
                    queue.put(v)
                    visited.add(v)
        return False



if __name__ == '__main__':
    import sys

    graph = ListGraph()
    for i in [1, 2, 3, 20, 39, 120]:
        graph.add_vertex(i)

    graph.make_edge(1, 2)
    graph.make_edge(2, 3)
    graph.make_edge(3, 20)
    graph.make_edge(20, 39)
    graph.make_edge(39, 120)

    print('GRAPH CONSTRUCTED')

    print('Vertices:', graph.vertices())
    print('Number of vertices:', graph.num_vertices)
    print('Number of edges:', graph.num_edges)
    print('Edges:', graph.edges())
    print('Neighbours of vertex 2:', graph.neighbours(2))
    print('Size of the Graph:', sys.getsizeof(graph._graph_list))

    print('Depth first search of the path between 1 and 120:', graph.dfs(1, 120))
    print('Breath first search of the path between 1 and 120:', graph.bfs(1, 120))
