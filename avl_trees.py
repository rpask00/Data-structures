from ttictoc import TicToc
import random
import math


class AVL_Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.ln = None
            self.rn = None
            self.height = 0

    def __init__(self, value):
        self.root = self.Node(value)
        self.__height = 1

    def find(self, value):
        current = self.root
        while True:
            if value == current.value:
                return True

            if value > current.value:
                if current.rn:
                    current = current.rn
                else:
                    return False
            else:
                if current.ln:
                    current = current.ln
                else:
                    return False

    def insert(self, value):
        def __insert(value, node=None):
            if not node:
                return self.Node(value)

            if value < node.value:
                node.ln = __insert(value, node.ln)
            else:
                node.rn = __insert(value, node.rn)

            self.set_height(node)

            return self.balance(node)

        self.root = __insert(value, self.root)

    def balance(self, root):
        root.balance_factor = self.get_balance_factor(root)

        if self.isRightHeavy(root):
            if root.rn.balance_factor > 0:
                root.rn = self.right_rotation(root.rn)
            root = self.left_rotation(root)

        elif self.isLeftHeavy(root):
            if root.ln.balance_factor < 0:
                root.ln = self.left_rotation(root.ln)
            root = self.right_rotation(root)

        self.set_height(root)

        root.balance_factor = self.get_balance_factor(root)

        return root

    def left_rotation(self, root):
        newRoot = root.rn
        root.rn = newRoot.ln
        newRoot.ln = root

        self.set_height(root)
        self.set_height(newRoot)

        return newRoot

    def right_rotation(self, root):
        newRoot = root.ln
        root.ln = newRoot.rn
        newRoot.rn = root

        self.set_height(root)
        self.set_height(newRoot)

        return newRoot

    def set_height(self, node):
        node.height = max(self.get_height(node.ln),
                          self.get_height(node.rn)) + 1

    def get_height(self, node=None):
        return node.height if node else -1

    def isLeftHeavy(self, node):
        if self.get_balance_factor(node) > 1:
            return True

        return False

    def isRightHeavy(self, node):
        if self.get_balance_factor(node) < -1:
            return True

        return False

    def get_balance_factor(self, node):
        if not node:
            return 0

        return self.get_height(node.ln) - self.get_height(node.rn)

    def is_perfect(self, node=None):
        if not node:
            node = self.root

        if not node.ln and not node.rn:
            return True

        if not node.ln or not node.rn:
            return False

        if node.ln and node.rn:
            return [self.is_perfect(node.ln), self.is_perfect(node.rn)] == [True, True]


t = AVL_Tree(25)
t.insert(20)
t.insert(10)
t.insert(21)
t.insert(30)
t.insert(26)
t.insert(40)

print(t.is_perfect())

# clock = TicToc()
# clock.tic()

# for i in range(343):
#     t.insert(random.randint(2, 34534534))

# clock.toc()
# print(clock.elapsed)
