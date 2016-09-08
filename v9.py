from util import combine_dictionaries
from trie import Trie


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
    combine_dictionaries,
    ({letter: num for letter in letters} for letters, num in V9_SPEC)
)


if __name__ == '__main__':
    trie = Trie(mapping=lambda x: V9_LETTER_TO_NUM[x])

    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            trie.insert(line.lower().strip())

    print trie.get_words('43556')
    print trie.get_words('222783')
    print trie.get_words('8378464')
