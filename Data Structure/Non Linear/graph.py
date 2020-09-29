class Node:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return str(self.label)


class Graph:
    def __init__(self):
        self.counter = 0
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        node = Node(label)
        if self.nodes.get(label) is None:
            self.nodes[label] = node
        if self.adjacency_list.get(node) is None:
            self.adjacency_list[node] = []

    def add_edge(self, f, t):
        from_node = self.nodes.get(f)
        if from_node is None:
            raise IndexError("Node not found")

        to_node = self.nodes.get(t)
        if to_node is None:
            raise IndexError("Node not found")

        self.adjacency_list.get(from_node).append(to_node)

    def remove_node(self, label):
        node = self.nodes.get(label)
        if node is None:
            return

        for n in self.adjacency_list.keys():
            node_list = self.adjacency_list.get(n)
            if len(node_list) > 0 and node_list.__contains__(node):
                node_list.remove(node)

        self.adjacency_list.pop(node)
        self.nodes.pop(label)

    def remove_edge(self, f, t):
        from_node = self.nodes.get(f)
        if from_node is None:
            raise IndexError("Node not found")

        to_node = self.nodes.get(t)
        if to_node is None:
            raise IndexError("Node not found")

        self.adjacency_list.get(from_node).remove(to_node)

    def print_list(self):
        for source in self.adjacency_list.keys():
            targets = self.adjacency_list.get(source)
            if len(targets) > 0:
                print(f"{source} is connected with {targets}")


if __name__ == "__main__":
    graph = Graph()
    graph.add_node('azhar')
    graph.add_node('sohaib')
    graph.add_node('hassin')
    graph.add_edge('azhar', 'sohaib')
    graph.add_edge('azhar', 'hassin')
    graph.add_edge('sohaib', 'hassin')
    graph.remove_node('sohaib')

    graph.print_list()
