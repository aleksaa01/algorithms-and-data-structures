from queue import Queue


class MappedGraph(object):

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

        if directed or vertex1 == vertex2:
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

    def neighbours(self, vertex):
        try:
            return self._graph_dict[vertex]
        except AttributeError:
            raise ValueError('Vertex({}) not found in Graph.'.format(vertex))

    def edges(self):
        edges = [None] * self.num_edges
        count = 0
        for node in self._graph_dict:
            for neighbour in self._graph_dict[node]:
                edges[count] = (node, neighbour)
                count += 1
        return edges

    def dfs(self, source, destination):
        visited = set()
        visited.add(source)
        return self._dfs(source, destination, visited)

    def _dfs(self, source, destination, visited):
        if source == destination:
            return True

        for node in self.neighbours(source):
            if node in visited:
                continue
            visited.add(node)
            found = self._dfs(node, destination, visited)
            if found:
                return True

        return False

    def bfs(self, source, destination):
        queue = Queue()
        visited = set()

        queue.put(source)
        visited.add(source)
        while not queue.empty():
            for node in self.neighbours(queue.get()):
                if node == destination:
                    return True
                elif node not in visited:
                    queue.put(node)
                    visited.add(node)
        return False




if __name__ == '__main__':
    graph = MappedGraph()
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
    print('Depth first search of the path between a and e:', graph.dfs('a', 'e'))
    print('Breadth first search of the path between a and e:', graph.bfs('a', 'e'))
    print('Depth first search of the path between a and f:', graph.dfs('a', 'f'))
    print('Breadth first search of the path between a and f:', graph.bfs('a', 'f'))
