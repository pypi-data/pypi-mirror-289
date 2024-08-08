import string

chars = set(string.ascii_lowercase + string.digits)


def _tri_sub(word):
    padded = f'  {word} '
    return set(padded[i:i+3] for i in range(len(padded)-2))


def tri_gen(word):
    tri = set()
    sym_swapped = ''.join(c if c in chars else ' ' for c in word.lower())
    for sub in sym_swapped.split():
        if not sub:
            continue

        tri = tri.union(_tri_sub(sub))

    return frozenset(tri)


def tri_compare(word1: str, word2: str):
    """generate trigrams for and return overall similarity between them. order irrelevant"""
    return tri_calc(tri_gen(word1), tri_gen(word2))


def tri_compare_word_similarity(word1: str, word2: str):
    """generate trigrams for and return substring similarity between them. result is relative to word1"""
    return tri_calc_ws(tri_gen(word1), tri_gen(word2))


def tri_calc(tri1: set | frozenset, tri2: set | frozenset):
    """calculates overall similarity of two trigrams"""
    try:
        return len(tri1.intersection(tri2)) / len(tri1.union(tri2))
    except ZeroDivisionError:
        return 0.0


def tri_calc_ws(tri1: set | frozenset, tri2: set | frozenset):
    """calculates word similarity (substring analysis) of two trigrams"""
    if not (d := len(tri1)):
        return 0.0

    return len(tri1.intersection(tri2)) / d


def tri_calc_bws(tri1: set | frozenset, tri2: set | frozenset, threshold: float = .8):
    """bi-directional substring analysis"""
    return tri_calc_ws(tri1, tri2) >= threshold or tri_calc_ws(tri2, tri1) >= threshold

