from util import combine_dictionaries
from trie import Trie


V9_SPEC = (
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
    combine_dictionaries,
    ({letter: num for letter in letters} for letters, num in V9_SPEC)
)


if __name__ == '__main__':
    trie = Trie(mapping=lambda x: V9_LETTER_TO_NUM[x])
    trie.insert('hi')
    trie.insert('bye')
    trie.print_subtree()

    with open('/usr/share/dict/words'):
        pass
