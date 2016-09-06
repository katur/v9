from util import combine_dictionaries, identity, indent


V9_MAPPING = (
    ('abc', 2),
    ('def', 3),
    ('ghi', 4),
    ('jkl', 5),
    ('mno', 6),
    ('pqrs', 7),
    ('tuv', 8),
    ('wxyz', 9),
)


LETTER_TO_NUM = reduce(
    combine_dictionaries,
    ({letter: num for letter in letters} for letters, num in V9_MAPPING)
)


def v9_mapping(letter):
    return LETTER_TO_NUM(letter)


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

        for letter in word:
            mapped = self.mapping[letter]

            if mapped not in node.children:
                node.children[mapped] = Node(mapped)

            node = node.children[mapped]

        node.items.add(word)

    def print_subtree(self):
        self.root.print_subtree(0)


class Node():

    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.items = set()

    def __str__(self):
        s = 'Node:{}'.format(self.key)

        if self.items:
            s += ' ({})'.format(','.join(self.items))

        return s

    def __repr__(self):
        return str(self)

    def print_subtree(self, indent_level):
        print indent(self, indent_level)

        for key, node in self.children.iteritems():
            node.print_subtree(indent_level + 1)


if __name__ == '__main__':
    trie = Trie(mapping=LETTER_TO_NUM)
    trie.insert('hi')
    trie.insert('bye')
    trie.print_subtree()

    with open('/usr/share/dict/words'):
        pass
