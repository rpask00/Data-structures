from ttictoc import TicToc
import random


class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.ln = None
            self.rn = None
            self.height = 0

    def __init__(self, value):
        self.root = self.Node(value)
        self.is_balanced = True

    def insert(self, value):
        current = self.root
        self.set_height(current)
        current.balance_factor = self.get_balance_factor(current)
        while True:
            if value > current.value:
                if current.rn:
                    current = current.rn
                else:
                    current.rn = self.Node(value)
                    self.set_height(current)
                    current.balance_factor = self.get_balance_factor(current)
                    break
            else:
                if current.ln:
                    current = current.ln
                else:
                    current.ln = self.Node(value)
                    self.set_height(current)
                    current.balance_factor = self.get_balance_factor(current)
                    break
                
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

    def isLeaf(self, root):
        if not root.ln and not root.rn:
            return True

        return False

    def depth_first(self):
        order = []

        def inner_depth_first(node):
            if node is None:
                return

            order.append(node.value)
            inner_depth_first(node.ln)
            inner_depth_first(node.rn)

        inner_depth_first(self.root)
        return order

    def minimum_value(self, node=None):
        if not node:
            node = self.root

        if not node.ln:
            return node.value

        return self.minimum_value(node.ln)

    def maximum_value(self, node=None):
        if not node:
            node = self.root

        if not node.rn:
            return node.value

        return self.maximum_value(node.rn)

    def equality_checking(self, potential_tree_root, myroot=None):
        if not myroot:
            myroot = self.root

        if not myroot.value is potential_tree_root.value:
            return False

        if self.isLeaf(myroot) and self.isLeaf(potential_tree_root):
            return myroot.value == potential_tree_root.value

        if not self.isLeaf(myroot) and not self.isLeaf(potential_tree_root):
            ml = myroot.ln
            mr = myroot.rn
            pl = potential_tree_root.ln
            pr = potential_tree_root.rn
            my_root_table = [bool(ml), bool(mr)]

            if not my_root_table == [bool(pl), bool(pr)]:
                return False

            if my_root_table == [False, True]:
                return [True, self.equality_checking(pr, mr)] == [True, True]

            if my_root_table == [True, False]:
                return [self.equality_checking(pl, ml), True] == [True, True]

            if my_root_table == [True, True]:
                return [self.equality_checking(pl, ml), self.equality_checking(pr, mr)] == [True, True]

        return False

    def kth_nodes(self, k_node):
        res = []
        def find_nodes(k, node):
            if node is None:
                node = self.root

            if k == 1:
                res.append(node.value)
                return

            if node.ln:
                find_nodes(k-1, node.ln)

            if node.rn:
                find_nodes(k-1, node.rn)

        find_nodes(k_node, self.root)

        return res

    def get_height(self,  node=None, n=1):
        if not node:
            node = self.root

        if self.__height < n:
            self.__height = n

        if self.isLeaf(node):
            return

        if node.ln:
            self.get_height(node.ln, n+1)
        if node.rn:
            self.get_height(node.rn, n + 1)

        return self.__height

    def lot_traversing(self):
        lot = []
        for i in range(1, self.get_height()+1):
            lot += self.kth_nodes(i)

        return lot

    def areSiblings(self, a, b, node=None):
        if not node:
            node = self.root

        if not node.ln or not node.rn:
            return False

        if [node.ln.value, node.rn.value] == sorted([a, b]):
            return True

        if self.areSiblings(a, b, node.ln) or self.areSiblings(a, b, node.rn):
            return True

        return False

    def is_perfect(self, node=None):
        if not node:
            node = self.root

        if not node.ln and not node.rn:
            return True

        if not node.ln or not node.rn:
            return False

        if node.ln and node.rn:
            return [self.is_perfect(node.ln), self.is_perfect(node.rn)] == [True, True]

    def set_height(self, node):
        node.height = max(self.get_height(node.ln),
                          self.get_height(node.rn)) + 1

    def get_height(self, node=None):
        return node.height if node else -1

    def get_balance_factor(self, node):
        if not node:
            return 0

        balance = self.get_height(node.ln) - self.get_height(node.rn)
        if balance > 1 or balance < -1:
            self.is_balanced = False

        return balance


t = Tree(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)


clock = TicToc()
clock.tic()

for i in range(32424):
    t.insert(random.randint(2, 34534534))

clock.toc()
print(clock.elapsed)
print(t.is_balanced)