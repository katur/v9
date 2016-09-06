from util import identity, indent


class Trie():

    def __init__(self, mapping=identity):
        self.mapping = mapping
        self.root = Node()

    def __str__(self):
        return 'Trie with root {}'.format(self.root)

    def __repr__(self):
        return str(self)

    def insert(self, word):
        node = self.root

        for char in word:
            mapped = self.mapping(char)

            if mapped not in node.children:
                node.children[mapped] = Node(mapped)

            node = node.children[mapped]

        node.words.add(word)

    def print_subtree(self):
        self.root.print_subtree(0)


class Node():

    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.words = set()

    def __str__(self):
        s = 'Node:{}'.format(self.key)

        if self.words:
            s += ' ({})'.format(','.join(self.words))

        return s

    def __repr__(self):
        return str(self)

    def print_subtree(self, indent_level):
        print indent(self, indent_level)

        for key, node in self.children.iteritems():
            node.print_subtree(indent_level + 1)
