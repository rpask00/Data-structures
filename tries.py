import requests
from ttictoc import TicToc


class Trie:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.childrens = {}
            self.isEndOftheWord = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word):
        self.__insert(word, self.root)

    def __insert(self, word, node):
        if not word:
            node.isEndOftheWord = True
            return

        currentLetter = word[0]
        if currentLetter not in node.childrens:
            node.childrens[currentLetter] = self.Node(currentLetter)

        next_node = node.childrens[currentLetter]
        return self.__insert(word[1:], next_node)

    def contains(self, word):
        return self.__contains(word, self.root)

    def __contains(self, word, node):
        if not word:
            return node.isEndOftheWord

        currentLetter = word[0]
        if currentLetter not in node.childrens:
            return False

        next_node = node.childrens[currentLetter]
        return self.__contains(word[1:], next_node)

    def traverse(self):
        self.__traverse(self.root)

    def __traverse(self, node):
        print(node.value)

        for key in node.childrens.keys():
            self.__traverse(node.childrens[key])

    def remove_word(self, word):
        if not word or not self.contains(word):
            return

        self.__remove_word(word, self.root)

    def __remove_word(self, word, node):
        if word:
            currentLetter = word[0]
            nxt_node = node.childrens[currentLetter]

            if not self.__remove_word(word[1:], nxt_node):
                node.childrens.pop(currentLetter)
        else:
            node.isEndOftheWord = False

        return node.childrens or node.isEndOftheWord

    def auto_complete(self, prefix):
        if not prefix:
            return []

        last_letter_node = self.root

        for w in prefix:
            last_letter_node = last_letter_node.childrens[w]

        return self.__auto_complete(last_letter_node, word[:-1])

    def __auto_complete(self, node, prefix, prev=[]):
        prefix += node.value

        if node.isEndOftheWord:
            prev.append(prefix)

        for key in node.childrens.keys():
            next_node = node.childrens[key]
            prev = self.__auto_complete(next_node, prefix, prev)

        return prev

    def count_words(self):
        return self.__count_words(self.root)

    def __count_words(self, node, count=0):
        if node.isEndOftheWord:
            count += 1

        for key in node.childrens.keys():
            nxt_node = node.childrens[key]

            count = self.__count_words(nxt_node, count)

        return count


t = Trie()
clock = TicToc()
db = requests.get(
    'https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').json().keys()

for d in db:
    t.insert(d)

clock.tic()
print(t.count_words())
clock.toc()

print(clock.elapsed)

