from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')
q.append('d')
q.append('e')
q.append('f')


def reverse_que(que):
    stack = []

    while len(que):
        stack.append(que.popleft())

    while len(stack):
        que.append(stack.pop())

    return que


class Que:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, data):
        if not self.stack_2 and not self.stack_1:
            return

        if not self.stack_1:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())

        self.stack_1.append(data)

    def dequeue(self):
        if not self.stack_2 and not self.stack_1:
            return

        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

        self.stack_2.pop()

    def peek(self):
        if not self.stack_2 and not self.stack_1:
            raise IndexError()

        if not self.stack_1:
            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())

        return self.stack_1


class Linked_List_Que:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = self.head = self.Node()

    def enqueue(self, data):
        if not self.first.data:
            self.first.data = data
            return data

        self.head.next = self.Node(data)
        self.head = self.head.next
        return data

    def dequeue(self):
        if not self.first:
            raise IndexError()

        return_Data = self.first.data
        self.first = self.first.next

        return return_Data

    def print_que(self):
        current = self.first

        while current:
            print(current.data)
            current = current.next


lque = Linked_List_Que()
lque.enqueue(45)
lque.enqueue(34)
lque.enqueue(46)
lque.enqueue(23)
lque.enqueue(95)


lque.dequeue()


lque.print_que()



class Priority_que:
    def __init__(self):
        self.que = [1, 2, 3, 4, 7, 8, 9]

    def enqueue(self, value):
        que = self.que
        if not que or que[-1] <= value:
            que.append(value)
            return value
        else:
            que.append(que[-1])

        for i in range(len(que) - 2, 0, -1):
            if que[i] > value:
                que[i] = que[i - 1]
                if que[i] <= value:
                    que[i] = value
                    return value

        que[0] = value

    def dequeue(self):
        if not self.que:
            raise IndexError()

        self.que.pop(0)

    def reverse_k_elements(self, k):
        stack = []
        for i in range(k):
            stack.append(self.que[i])

        insert_index = 0
        while stack:
            self.que[insert_index] = stack.pop()
            insert_index += 1

        return self.que


q = Priority_que()
