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


def combine_dictionaries(a, b):
    return dict(a.items() + b.items())


LETTER_TO_NUM = reduce(
    combine_dictionaries,
    ({letter: num for letter in letters} for letters, num in V9_MAPPING)
)


def v9_mapping(letter):
    return LETTER_TO_NUM(letter)


def identity(letter):
    return letter


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

        for letter, node in self.children.iteritems():
            node.print_subtree(indent_level + 1)


def indent(s, indent_level):
    return '{}{}'.format('\t' * indent_level, s)


if __name__ == '__main__':
    trie = Trie(mapping=LETTER_TO_NUM)
    trie.insert('hi')
    trie.insert('bye')
    trie.print_subtree()

    with open('/usr/share/dict/words'):
        pass
