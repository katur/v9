class Trie():

    def __init__(self, mapping=lambda x: x):
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

    def get_words(self, key_seq):
        node = self.root

        for key in key_seq:
            try:
                key = int(key)
            except ValueError:
                raise ValueError('{} is not an int (key_seq must be '
                                 'comprised of ints)'.format(key))

            if key not in node.children:
                return set()

            node = node.children[key]

        return node.words

    def print_trie(self):
        self.root.print_subtrie(indent_level=0)


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

    def print_subtrie(self, indent_level):
        print '{}{}'.format('\t' * indent_level, self)

        for key, node in self.children.iteritems():
            node.print_subtrie(indent_level + 1)
