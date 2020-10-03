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

    def get_shortest_distance(self, f, t):
        pass

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
    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'C', 2)
    graph.print_list()
