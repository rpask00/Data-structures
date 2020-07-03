import math


class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap)-1
        parent_index = (index-1)//2

        while index and self.heap[parent_index] < value:
            self.__swap_values(parent_index, index)
            index = parent_index
            parent_index = (index-1)//2

        return self.heap

    def __swap_values(self, parent_index, index, arr=None):
        if not arr:
            arr = self.heap

        bufor_value = arr[parent_index]
        arr[parent_index] = arr[index]
        arr[index] = bufor_value

    def __index_of_greater_value(self, left, right, arr=None):
        if not arr:
            arr = self.heap

        last_index = len(arr)-1

        if left > last_index and right > last_index:
            return 0

        if left > last_index:
            return right

        if right > last_index:
            return left

        return left if arr[left] > arr[right] else right

    def remove(self):
        removed_Value = self.heap[0]

        index = len(self.heap)-1

        self.__swap_values(0, index)
        self.heap.pop()

        parent = 0

        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2

            index = self.__index_of_greater_value(left, right)
            if not index or self.heap[parent] >= self.heap[index]:
                break

            self.__swap_values(parent, index)

            parent = index

        return removed_Value

    def heapify(self, arr):
        for i in range(len(arr)):
            self.__heapify(i, arr)

        return arr

    def __heapify(self, parent, arr):
        left = 2 * parent + 1
        right = 2 * parent + 2

        larger_index = self.__index_of_greater_value(left, right, arr)

        if larger_index and arr[larger_index] > arr[parent]:
            self.__swap_values(parent, larger_index, arr)
        else:
            return

        self.__heapify(larger_index, arr)

    def kth_largrst_item(self, k):
        if k < 0 or k >= len(self.heap):
            raise IndexError()

        heap = self.heap.copy()

        for i in range(k-1):
            self.remove()

        return_value = self.heap[0]
        self.heap = heap

        return return_value


h = Heap()

h.insert(15)
h.insert(10)
h.insert(3)
h.insert(8)
h.insert(12)
h.insert(9)
h.insert(4)
h.insert(1)
h.insert(24)

print(h.kth_largrst_item(44))
