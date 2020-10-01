from collections import deque


class Node:
    def __init__(self, label):
        self.label = label

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

    def traverse_dfs(self, root):
        node = self.nodes.get(root)
        if node is None:
            return
        self.__traverse_dfs(node, set())

    def __traverse_dfs(self, node, visited):
        print(node)
        visited.add(node)

        for n in self.adjacency_list.get(node):
            if not visited.__contains__(n):
                self.__traverse_dfs(n, visited)

    def traverse_dfs_iter(self, root):
        node = self.nodes.get(root)
        if node is None:
            return

        stack = []
        visited = set()
        stack.append(node)

        while len(stack) > 0:
            current = stack.pop()

            if visited.__contains__(current):
                continue

            print(current)
            visited.add(current)

            for neighbours in self.adjacency_list.get(current):
                if not visited.__contains__(neighbours):
                    stack.append(neighbours)

    def traverse_bfs_iter(self, root):
        node = self.nodes.get(root)
        if node is None:
            return

        visited = set()
        queue = deque()
        queue.append(node)

        while len(queue) > 0:
            current = queue.popleft()

            if visited.__contains__(current):
                continue
            print(current)
            visited.add(current)

            for neighbours in self.adjacency_list.get(current):
                if not visited.__contains__(neighbours):
                    queue.append(neighbours)

    def topological_sort(self, root):
        stack = []
        visited = set()

        for n in self.nodes.values():
            self.__topological_sort(n, visited, stack)

        sorted_list = []
        while len(stack) > 0:
            sorted_list.append(stack.pop())
        return sorted_list

    def __topological_sort(self, node, visited, stack):
        if visited.__contains__(node):
            return

        visited.add(node)

        for neighbours in self.adjacency_list.get(node):
            self.__topological_sort(neighbours, visited, stack)

        stack.append(node)

    def has_cycle(self):
        all_nodes = set()
        visiting = set()
        visited = set()

        for n in self.nodes.values():
            all_nodes.add(n)

        while len(all_nodes) > 0:
            current = next(iter(all_nodes))
            if self.__has_cycle(current, all_nodes, visiting, visited):
                return True

        return False

    def __has_cycle(self, node, all_nodes, visiting, visited):
        all_nodes.remove(node)
        visiting.add(node)

        for neighbour in self.adjacency_list.get(node):
            if visited.__contains__(neighbour):
                continue

            if visiting.__contains__(neighbour):
                return True
            if self.__has_cycle(neighbour, all_nodes, visiting, visited):
                return True

        visiting.remove(node)
        visited.add(node)
        return False


if __name__ == "__main__":
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')

    print(graph.has_cycle())
