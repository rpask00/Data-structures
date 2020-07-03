import sys


class PriorityQue:
    def __init__(self):
        self.que = []

    def enqueue(self, node):

        value = node.priority

        que = self.que
        if not que or que[-1].priority <= value:
            que.append(node)
            return value
        else:
            que.append(que[-1])

        for i in range(len(que) - 2, 0, -1):
            if que[i].priority > value:
                que[i] = que[i - 1]
                if que[i].priority <= value:
                    que[i] = node
                    return value

        que[0] = node

    def dequeue(self):
        if not self.que:
            raise IndexError()

        return self.que.pop(0)

    def isEmpty(self):
        return False if self.que else True

    def reverse_k_elements(self, k):
        stack = []
        for i in range(k):
            stack.append(self.que[i])

        insert_index = 0
        while stack:
            self.que[insert_index] = stack.pop()
            insert_index += 1

        return self.que


class PriorityQue_forEdges:
    def __init__(self):
        self.que = []

    def dequeueAll(self):
        self.que = []

    def enqueue(self, edge):

        value = edge.weight

        que = self.que
        if not que or que[-1].weight <= value:
            que.append(edge)
            return value
        else:
            que.append(que[-1])

        for i in range(len(que) - 2, 0, -1):
            if que[i].weight > value:
                que[i] = que[i - 1]
                if que[i].weight <= value:
                    que[i] = edge
                    return value

        que[0] = edge

    def dequeue(self):
        if not self.que:
            raise IndexError()

        return self.que.pop(0)

    def isEmpty(self):
        return False if self.que else True

    def reverse_k_elements(self, k):
        stack = []
        for i in range(k):
            stack.append(self.que[i])

        insert_index = 0
        while stack:
            self.que[insert_index] = stack.pop()
            insert_index += 1

        return self.que


class Weighted_Graphs:
    class NodeEntry:
        def __init__(self, node, priority):
            self.node = node
            self.priority = priority

    class Node:
        class Edge:
            def __init__(self, from_, to_, weight):
                self.from_ = from_
                self.to_ = to_
                self.weight = weight

            def __str__(self):
                return f'{self.from_}->{self.to_}'

        def __init__(self, label):
            self.label = label
            self.edges = []

        def addEdge(self, to_, weight):
            self.edges.append(self.Edge(self, to_, weight))

        def __str__(self):
            return self.label

    class Path:
        def __init__(self, from_, to_):
            self.from_ = from_
            self.to_ = to_
            self.path = []

        def add_node(self, node):
            self.path.append(node.label)

    def __init__(self):
        self.nodes = {}

    def addNode(self, label):
        self.nodes[label] = self.Node(label)

    def addEdge(self, from_, to_, weight=1):
        if from_ not in self.nodes.keys() or to_ not in self.nodes.keys():
            raise InterruptedError()

        from_ = self.nodes[from_]
        to_ = self.nodes[to_]

        from_.addEdge(to_, weight)
        to_.addEdge(from_, weight)

    def print_connections(self):
        for key in self.nodes:
            node = self.nodes[key]
            connections = [edge.to_.label for edge in node.edges]
            print(key, 'is connected to: ', connections)

    def __get_path(self, from_, to_, previousNodes):
        current = self.nodes[to_]
        stack = []

        while current is not self.nodes[from_]:
            stack.append(current)
            current = previousNodes[current]

        stack.append(current)
        p = self.Path(from_, to_)

        while stack:
            p.add_node(stack.pop())

        return p

    def find_shortest_path(self, from_, to_, visited=set()):
        distances = {}
        que = PriorityQue()
        previousNodes = {}

        # calculating default distances
        for node in self.nodes.values():
            if node.label == from_:
                distances[node] = 0
                que.enqueue(self.NodeEntry(node, 0))
            else:
                distances[node] = sys.maxsize

        while not que.isEmpty():
            node = que.dequeue().node
            visited.add(node)

            for edge in node.edges:
                if edge.to_ in visited:
                    continue

                newDistance = distances[node] + edge.weight
                if newDistance < distances[edge.to_]:
                    distances[edge.to_] = newDistance
                    que.enqueue(self.NodeEntry(edge.to_, newDistance))
                    previousNodes[edge.to_] = node

        return self.__get_path(from_, to_, previousNodes)

    def dijkstra(self, from_, to_, visited=set()):
        p = self.Path(from_, to_)
        distances = {}
        que = []

        for key in self.nodes.keys():
            node = self.nodes[key]
            if key == from_:
                distances[node] = {
                    'distance': 0,
                    'last': ''
                }
                que.append(node)
            else:
                distances[node] = {
                    'distance': sys.maxsize,
                    'last': ''
                }

        while que:
            node = que.pop(0)
            visited.add(node)

            for edge in node.edges:
                if edge.to_ not in visited:
                    que.append(edge.to_)

                    newDistance = distances[node]['distance'] + edge.weight
                    if distances[edge.to_]['distance'] > newDistance:
                        distances[edge.to_]['distance'] = newDistance
                        distances[edge.to_]['last'] = node

        current = self.nodes[to_]
        while current != self.nodes[from_]:
            p.add_node(current)
            current = distances[current]['last']

        p.add_node(current)

        return p.path, distances[self.nodes[to_]]['distance']

    def hasCycle(self):
        visited = set()
        for node in self.nodes.values():
            if node in visited:
                continue

            que = [(node, node)]

            while que:
                node, previous = que.pop(0)
                visited.add(node)

                for edge in node.edges:
                    if edge.to_ in visited and previous is not edge.to_:
                        return True

                    if edge.to_ not in visited:
                        que.append((edge.to_, node))

        return False

    def __get_first_node(self):
        for node in self.nodes.values():
            return node

    def get_spanning_tree(self):
        que = PriorityQue_forEdges()
        visited = set()
        edges = []

        node = self.__get_first_node()

        while True:
            visited.add(node)
            for edge in node.edges:
                if edge.to_ not in visited and edge.from_ in visited:
                    que.enqueue(edge)

            if que.isEmpty():
                break

            currentEdge = que.dequeue()
            edges.append(currentEdge)
            que.dequeueAll()

            node = currentEdge.to_

        return edges


wg = Weighted_Graphs()

wg.addNode('A')
wg.addNode('B')
wg.addNode('C')
wg.addNode('D')
# wg.addNode('D')
# wg.addNode('E')

# wg.addEdge('A', 'D', 3)
# wg.addEdge('A', 'C', 4)
# wg.addEdge('A', 'B', 2)
# wg.addEdge('B', 'D', 6)
# wg.addEdge('C', 'B', 1)
# wg.addEdge('B', 'E', 5)
# wg.addEdge('D', 'E', 1)

wg.addEdge('A', 'B', 3)
wg.addEdge('A', 'C', 1)
wg.addEdge('B', 'D', 4)
wg.addEdge('B', 'C', 2)
wg.addEdge('D', 'C', 5)




for edge in wg.get_spanning_tree():
    print(edge)
