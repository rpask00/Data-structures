class Node:
    class Edge:
        def __init__(self, from_, to_, weight):
            self.from_ = from_
            self.to_ = to_
            self.weight = weight

    def __init__(self, label):
        self.label = label
        self.edges = []

    def addEdge(self, to_, weight):
        self.edges.append(self.Edge(self, to_, weight))

    def __str__(self):
        return self.label

    def __dict__(self):
        return self.label


n = Node('a')
print(n)
