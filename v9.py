T9_MAPPING = (
    ('abc', 2),
    ('def', 3),
    ('ghi', 4),
    ('jkl', 5),
    ('mno', 6),
    ('pqrs', 7),
    ('tuv', 8),
    ('wxyz', 9),
)


class Trie():

    def __init__(self):
        self.root = Node()

    def __str__(self):
        return 'Trie with root {}'.format(self.root)

    def __repr__(self):
        return str(self)

    def insert(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node(letter)

            node = node.children[letter]

        node.words.add(word)

    def print_subtree(self):
        self.root.print_subtree(0)


class Node():

    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.words = set()

    def __str__(self):
        s = 'Node letter:{}'.format(self.letter)
        if self.words:
            s += ' words: {}'.format(self.words)
        return s

    def __repr__(self):
        return str(self)

    def print_subtree(self, indent):
        print '{}{}'.format('\t' * indent, self)

        for letter, node in self.children.iteritems():
            node.print_subtree(indent + 1)


def get_letter_to_num_dictionary():
    return reduce(
        combine_dictionaries,
        ({letter: num for letter in letters} for letters, num in T9_MAPPING)
    )


def combine_dictionaries(a, b):
    return dict(a.items() + b.items())


def indent_string(s, indent_level):
    return '{}{}'.format('t' * indent_level, s)


if __name__ == '__main__':
    letter_to_num = get_letter_to_num_dictionary()

    trie = Trie()
    trie.insert('hi')
    trie.insert('bye')
    trie.print_subtree()

    with open('/usr/share/dict/words'):
        pass
