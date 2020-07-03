class Graph:
    class Node:
        def __init__(self, label):
            self.label = label

    def __init__(self):
        self.nodes = {}
        self.adjacency_list = {}

    def addNode(self, label):
        node = self.Node(label)
        self.nodes[label] = node
        self.adjacency_list[node] = []

    def addEdge(self, from_, to_):
        from_node = self.nodes[from_]
        to_node = self.nodes[to_]

        if not from_node or not to_node:
            raise InterruptedError()

        if from_node not in self.adjacency_list.keys():
            self.adjacency_list[from_node] = []

        self.adjacency_list[from_node].append(to_node)

    def print_connections(self):
        for key in self.adjacency_list.keys():
            connections = [node.label for node in self.adjacency_list[key]]
            print(key.label, 'is connected to: ', connections)

    def removeNode(self, label):
        if label not in self.nodes.keys():
            return

        for a in self.adjacency_list:
            a.remove(self.nodes[label])

        self.nodes.pop(label)

    def removeEdge(self, from_, to_):
        from_node = self.nodes[from_]
        to_node = self.nodes[to_]

        if not from_node or not to_node:
            return

        self.adjacency_list[from_node].remove(self.nodes[to_node])

    def depth_first_traversing(self, start_label):
        if start_label not in self.nodes.keys():
            return

        self.__depth_first_traversing(self.nodes[start_label], set())

    def __depth_first_traversing(self, node, visited):
        visited.add(node)
        current = self.adjacency_list[node]

        print(node.label)

        for c in current:
            if c not in visited:
                self.__depth_first_traversing(c, visited)

    def depth_first_traversing_iterative(self, start_label):
        stack = []
        current = self.nodes[start_label]
        visited = set()
        stack.append(current)

        while stack:
            current = stack.pop()
            visited.add(current)
            print(current.label)

            if current in self.adjacency_list.keys():
                for node in self.adjacency_list[current]:
                    if node not in visited:
                        stack.append(node)

    def breadth_first_traversing(self, start_label):
        if start_label not in self.nodes.keys():
            return

        self.__breadth_first_traversing(self.nodes[start_label], set())

    def __breadth_first_traversing(self, current, visited=set()):
        que = [current]

        while que:
            current = que.pop(0)
            visited.add(current)
            print(current.label)

            for neighbour in self.adjacency_list[current]:
                if neighbour not in visited and neighbour not in que:
                    que.append(neighbour)

    def topological_sort(self, start_label):
        if start_label not in self.nodes.keys():
            return

        return self.__topological_sort(self.nodes[start_label])

    def __topological_sort(self, node, visited=set(), result=[]):
        visited.add(node)
        adjacency_list = self.adjacency_list

        current = self.adjacency_list[node]

        for c in current:
            if c not in visited:
                self.__topological_sort(c, visited, result)

        result.append(node.label)
        return result

    def HAScycle(self):
        if not self.adjacency_list:
            return

        for node in self.adjacency_list.keys():
            return self.__HAScycle(node)

    def __HAScycle(self, node, visited=set(), visiting=set()):
        visiting.add(node)

        current = self.adjacency_list[node]

        for c in current:
            if c not in visited:

                if c in visiting or self.__HAScycle(c, visited, visiting):
                    return True

        visited.add(node)
        return False


g = Graph()

g.addNode('A')
g.addNode('B')

g.addNode('C')
g.addNode('D')


g.addEdge('A', 'B')
g.addEdge('A', 'D')
g.addEdge('A', 'C')
g.addEdge('B', 'C')
# g.addEdge('C', 'A')


print(g.breadth_first_traversing('A'))
