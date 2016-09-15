print 'Loading...'


CORPUS = '/usr/share/dict/words'

V9_SPEC = (
    ('-', 1),
    ('abc', 2),
    ('def', 3),
    ('ghi', 4),
    ('jkl', 5),
    ('mno', 6),
    ('pqrs', 7),
    ('tuv', 8),
    ('wxyz', 9),
)


V9_LETTER_TO_NUM = reduce(
    lambda x, y: dict(x.items() + y.items()),
    ({letter: num for letter in letters} for letters, num in V9_SPEC)
)


def get_v9_trie():
    trie = Trie(mapping=lambda x: V9_LETTER_TO_NUM[x])

    with open(CORPUS, 'r') as f:
        for line in f:
            trie.insert(line.lower().strip())

    return trie


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
                return None

            node = node.children[key]

        return node.words

    def print_trie(self):
        self.root.print_subtrie(0)


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


if __name__ == '__main__':
    trie = get_v9_trie()
    # print trie.get_words('43556')
    # print trie.get_words('222783')
    # print trie.get_words('8378464')


print 'Done loading'
