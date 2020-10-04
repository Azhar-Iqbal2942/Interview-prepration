import sys
import heapq


class Node:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __repr__(self):
        return f"{self.from_node} -> {self.to_node}"


class NodeEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return str(self.node)


class Path:
    def __init__(self):
        self.__nodes = []

    def __str__(self):
        return str(self.__nodes)

    def add(self, node):
        self.__nodes.append(node)


class WeightedGraph:
    def __init__(self):
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        node = Node(label)
        if self.nodes.get(label) is None:
            self.nodes[label] = node
        if self.adjacency_list.get(node) is None:
            self.adjacency_list[node] = []

    def add_edge(self, f, t, weight):
        from_node = self.nodes.get(f)
        if from_node is None:
            raise IndexError("Node not found")

        to_node = self.nodes.get(t)
        if to_node is None:
            raise IndexError("Node not found")

        self.adjacency_list.get(from_node).append(
            Edge(from_node, to_node, weight))
        self.adjacency_list.get(to_node).append(
            Edge(to_node, from_node, weight))

    def get_shortest_path(self, f, t): # f->From t-> To
        from_node = self.nodes.get(f)
        to_node = self.nodes.get(t)
        distances = {}
        for node in self.nodes.values():
            distances[node] = sys.maxsize
        distances[from_node] = 0

        visited = set()
        previous_nodes = {}
        queue = []
        queue.append(NodeEntry(from_node, 0))

        while len(queue) > 0:
            heapq.heapify(queue)
            current = queue.pop(0).node
            visited.add(current)

            for edge in self.adjacency_list.get(current):
                if visited.__contains__(edge.to_node):
                    continue
                new_distance = distances.get(current) + edge.weight
                if new_distance < distances.get(edge.to_node):
                    distances[edge.to_node] = new_distance
                    previous_nodes[edge.to_node] = current
                    queue.append(NodeEntry(edge.to_node, new_distance))

        # Now build the shortest path using stack
        stack = []
        stack.append(to_node)
        previous = previous_nodes.get(to_node)
        while previous is not None:
            stack.append(previous)
            previous = previous_nodes.get(previous)

        path = Path()
        while len(stack) > 0:
            path.add(stack.pop())

        return path

    def print_list(self):
        for source in self.adjacency_list.keys():
            targets = self.adjacency_list.get(source)
            if len(targets) > 0:
                print(f"{source} is connected with {targets}")


if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'B', 1)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('A', 'C', 10)
    print(graph.get_shortest_path('A', 'C'))
