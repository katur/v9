from trie import Trie


CORPUS = '/usr/share/dict/words'

T9_SPEC = (
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


T9_LETTER_TO_NUM = reduce(
    lambda x, y: dict(x.items() + y.items()),
    ({letter: num for letter in letters} for letters, num in T9_SPEC)
)


def init_t9_trie():
    trie = Trie(mapping=lambda x: T9_LETTER_TO_NUM[x])

    with open(CORPUS, 'r') as f:
        for line in f:
            trie.insert(line.lower().strip())

    return trie


if __name__ == '__main__':
    trie = init_t9_trie()
    print trie.get_words('43556')
    print trie.get_words('222783')
    print trie.get_words('8378464')
