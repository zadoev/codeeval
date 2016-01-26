__author__ = 'zadoev@gmail.com'
"""
sequence aabaa;aaa;aacaa - depends of order

"""

from itertools import permutations
import sys


def get_overlap(a, b):
    """
    From https://neil.fraser.name/news/2010/11/04/
    with small optimizations about 3% speed up


    >>> (get_overlap('a', 'b'), get_overlap('', ''))
    (0, 0)
    >>> get_overlap('a', 'ab')
    1
    >>> get_overlap('aa', 'ab')
    1
    >>> get_overlap('ab', 'aa')
    0
    >>> get_overlap('ababcab', 'bcab')
    4
    """
    a_length = len(a)
    b_length = len(b)
    min_len = 0

    if a_length == 0 or b_length == 0:
        return 0

    if a_length > b_length:
        a = a[-b_length:]
        min_len = b_length
    elif a_length < b_length:
        b = b[:a_length]
        min_len = a_length
    if a == b:
        return min_len

    best = 0
    length = 1
    f = b.find
    while True:
        pattern = a[-length:]
        found = f(pattern)
        if found == -1:
            return best
        length += found
        if pattern == b[:length]:
            best = length
            length += 1


class Item(object):
    def __init__(self, fragment):
        self.fragment = fragment
        self.connections = {}
        self.best_item = None
        self.best_overlap = 0

    def connect(self, another_item, overlap=None):
        """
        Make connection from current item to another

        >>> a = Item('ab')
        >>> a.best_overlap
        0
        >>> a.best_item is None
        True
        >>> b = Item('a')
        >>> a.connect(b)
        >>> a.best_overlap
        1
        >>> a.best_item == b
        True
        >>> a.connections[b] == 1
        True
        >>> a = Item('')
        >>> b = Item('')
        >>> a.connect(b)
        >>> not a.connections
        True

        :param another_item:
        :type another_item: Item
        :param overlap:
        :type overlap: int
        """

        if another_item == self:
            return

        if overlap is None:
            overlap = get_overlap(another_item.fragment, self.fragment)

        if overlap == 0:
            return

        self.connections[another_item] = overlap

        if overlap > self.best_overlap:
            self.best_item = another_item
            self.best_overlap = overlap

    def disconnect(self, another):
        """
        Removes connection from this object to another

        >>> a = Item('a')
        >>> b = Item('b')  # fragments here not important
        >>> c = Item('c')
        >>> a.connect(b, 1)
        >>> a.connect(c, 2)  # c best match
        >>> (a.best_overlap, a.best_item == c)
        (2, True)
        >>> a.disconnect(c)
        >>> (a.best_overlap, a.best_item==b)
        (1, True)


        :param another:
        :type another: Item
        :return:
        """
        is_best_deleted = self.best_item == another

        del self.connections[another]

        if is_best_deleted:
            self.rebuild_best()

    def rebuild_best(self):
        """
        called when best item deleted
        >>> a = Item('')
        >>> a.connections = {'a': 1, 'b': 2, 'c': 3}
        >>> a.rebuild_best()
        >>> (a.best_item, a.best_overlap)
        ('c', 3)
        """
        if not self.connections:
            self.best_item = None
            self.best_overlap = 0
            return

        self.best_item, self.best_overlap = sorted(
            self.connections.items(), key=lambda t: t[1], reverse=True
        )[0]


class Solver(object):
    def __init__(self, fragments):
        self.fragments = fragments
        self.len = len(self.fragments)
        self.prev_best = None

    @staticmethod
    def glue(a, b, overlap):
        return a + b[overlap:]

    @staticmethod
    def find_best(items):
        """
        Find longest overlap

        :param items: fragments tree
        :type items: list[Item]
        :return:
        """

        if not items:
            return ()

        longest = sorted(items, key=lambda i: i.best_overlap, reverse=True)[0]

        if longest.best_overlap == 0:
            return ()

        return longest, longest.best_item, longest.best_overlap

    def solve(self):

        # init data for solve
        items_map = {f: Item(f) for f in self.fragments}

        for (a, b) in permutations(self.fragments, 2):
            overlap = get_overlap(a, b)

            if overlap:
                items_map[b].connect(items_map[a], overlap)

        items = list(items_map.values())

        del items_map

        while True:
            best = self.find_best(items)

            if not best:
                break

            a, b, overlap = best

            result = Item(self.glue(b.fragment, a.fragment, overlap))

            for i in items:
                if a in i.connections:
                    i.disconnect(a)
                    i.connect(result)

                if b in i.connections:
                    i.disconnect(b)
                    i.connect(result)

            for i in b.connections.keys():
                result.connect(i)

            items.remove(a)
            items.remove(b)
            items.append(result)

        return sorted([i.fragment for i in items], reverse=True, key=len)[0]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            solver = Solver(line.strip().split(';'))
            print(solver.solve())
