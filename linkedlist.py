from ttictoc import TicToc


class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = self.head = self.Node()

    def listprint(self):
        print_value = self.first
        while print_value is not None:
            print(print_value.data)
            print_value = print_value.next

    def addLast(self, val):
        if self.isEmpty():
            self.first.data = val
            return

        nextnode = self.Node(val)
        self.head.next = nextnode
        self.head = nextnode

    def indexOf(self, value):
        index = 0
        curent = self.first
        while curent.next:
            if curent.data == value:
                return index
            curent = curent.next
            index += 1

        return - 1

    def contains(self, value):
        curent = self.first
        while curent.next:
            if curent.data == value:
                return True
            curent = curent.next

        return False

    def removeFirst(self):
        second = self.first.next

        if self.isEmpty():
            raise IndexError()

        self.first.next = None
        self.first = second

    def removeLast(self):
        if self.first == self.head or self.isEmpty():
            raise IndexError()

        self.head = self.gePrevious(self.head)
        self.head.next = None

    def gePrevious(self, node):
        current = self.first

        while current.next:
            if current.next == node:
                return current

            current = current.next

        return None

    def isEmpty(self):
        if self.first.data is None:
            return True

        return False

    def toArray(self):
        result = []
        current = self.first

        while current:
            result.append(current.data)
            current = current.next

        return result.copy()

    def reversing(self):
        if not self.first.next:
            return

        previous = self.first
        current = self.first.next

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        self.head = self.first
        self.head.next = None
        self.first = previous

    def getNode(self, index):
        index -= 1
        one = second = self.first

        # get the k-th nde from the beginning
        try:
            while index:
                second = second.next
                index -= 1
        except:
            raise IndexError

        while second.next:
            second = second.next
            one = one.next

        return one.data

    def getMiddle(self):
        one = second = self.first

        while True:
            if second and second.next and second.next.next:
                second = second.next.next
                one = one.next
            else:
                if second.next:
                    return one.data, one.next.data
                return one.data


list = LinkedList()

for i in range(12):
    list.addLast(i*10)


# t = TicToc()
# t.tic()
# list.reversing()
# t.toc()
# print(t.elapsed)
print(list.getMiddle())
print('----------------------')
list.listprint()

# print(list.toArray())
