def combine_dictionaries(x, y):
    return dict(x.items() + y.items())


def identity(x):
    return x


def indent(s, indent_level):
    return '{}{}'.format('\t' * indent_level, s)
