
def find_multi(example):
    set_example = set()
    for ee in example:
        if ee in set_example:
            return ee
        set_example.add(ee)

    return None


class Hash_Table:
    class Node:
        def __init__(self, entry=None):
            self.entry = entry
            self.next = None

    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.list = []
        self.size = 10

        for i in range(self.size):
            self.list.append(self.Node())

    def put(self, key, value):
        hash1 = key % self.size
        head = self.list[hash1]

        while True:
            if not head.entry:
                head.entry = self.Entry(key, value)
            elif head.entry.key == key:
                head.entry.value = value
            else:
                if not head.next:
                    break

                head = head.next
                continue

            return value

        if not head.entry:
            head.entry = self.Entry(key, value)
        else:
            head.next = self.Node(self.Entry(key, value))

        return value

    def get(self, key):
        hash1 = key % self.size
        head = self.list[hash1]

        if not head.entry:
            raise IndexError()

        while head.next:
            if head.entry.key == key:
                return head.entry.value

            head = head.next

        return head.entry.value

    def get_previous(self, first, node):
        if first == node:
            return False

        while first.next:
            if first.next == node:
                return first

            first = first.next

        raise IndexError()

    def remove(self, key):
        hash1 = key % self.size
        head = self.list[hash1]

        if head.entry.key == key:
            head.entry = None

        while head.next:
            if head.entry.key == key:
                self.get_previous(self.list[hash1], head).next = head.next
                return key

            head = head.next

        if head.entry.key == key:
            self.get_previous(self.list[hash1], head).next = None
            return key

        return -1


ht = Hash_Table()


ht.put(2, 'sfsfs')
ht.put(3, 'aaaaaaaaaa')
ht.put(23, 'bbbbbbbbbbb')
ht.put(13, 'ccccccccccccccc')
ht.put(8, 'dddddddddddd')
ht.put(6, 'aadfsesefsefsefsefsef')

print(ht.remove(13))

print(ht.get(13))
