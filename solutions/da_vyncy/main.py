__author__ = 'zadoev@gmail.com'
"""
sequens aabaa;aaa;aacaa - depends of order

"""


import sys

def commonOverlapIndexOf(text1, text2):
    """
    From https://neil.fraser.name/news/2010/11/04/

    """
    # Cache the text lengths to prevent multiple calls.

    text1_length = len(text1)
    text2_length = len(text2)
    min_len = 0
    # Eliminate the null case.
    if text1_length == 0 or text2_length == 0:
        return 0
        # Truncate the longer string.
    if text1_length > text2_length:
        text1 = text1[-text2_length:]
        min_len = text2_length
    elif text1_length < text2_length:
        text2 = text2[:text1_length]
        min_len = text1_length
        # Quick check for the worst case.
    if text1 == text2:
        return min_len

        # Start by looking for a single character match
    # and increase length until no match is found.
    best = 0
    length = 1
    f = text2.find
    while True:
        pattern = text1[-length:]
        found = f(pattern)
        if found == -1:
            return best
        length += found
        if pattern == text2[:length]:
            best = length
            length += 1


class Solver(object):
    def __init__(self, fragments):
        self.fragments = fragments
        self.len = len(self.fragments)
        self.prev_best = None

    def find_best(self):
        self.prev_best = None
        pairs = (None, None)
        max_overlap = 0

        for i in range(self.len -1):
            for j in range(i+1, self.len):
                a = self.fragments[i]
                b = self.fragments[j]
                reversed, overlap = self.overlap(a, b)
                if overlap > max_overlap:
                    if pairs != (None, None):
                        self.prev_best = pairs

                    max_overlap = overlap
                    if reversed:
                        pairs = (j, i)
                    else:
                        pairs = (i, j)

        return max_overlap, pairs[0], pairs[1]

    def find_best_partial(self):
        if self.prev_best is None:
            return 0, None, None

        pairs = self.prev_best
        self.prev_best = None
        max_overlap = 0

        for i in range(self.len -1):
            j = self.len -1
            a = self.fragments[i]
            b = self.fragments[j]
            reversed, overlap = self.overlap(a, b)
            if overlap > max_overlap:

                if pairs != (None, None):
                    self.prev_best = pairs

                if reversed:
                    pairs = (j, i)
                else:
                    pairs = (i, j)

                max_overlap = overlap

        return max_overlap, pairs[0], pairs[1]

    def glue(self, overlap, a, b):
        return self.fragments[a] + self.fragments[b][overlap:]

    def overlap(self, a, b):
        overlap = commonOverlapIndexOf(a, b)
        back_overlap = commonOverlapIndexOf(b, a)

        if ( back_overlap > overlap ):
            return True, back_overlap
        else:
            return False, overlap

    def solve(self):
        while self.fragments:
            overlap, a, b = self.find_best()
            if overlap == 0:
                return sorted(self.fragments, reverse=True, key=len)[0]
            r = self.glue(overlap, a, b)

            del self.fragments[max(a,b)]
            del self.fragments[min(a, b)]
            self.fragments.append(r)

            self.len -= 1

            overlap, a, b = self.find_best_partial()

            if overlap == 0:
                continue

            r = self.glue(overlap, a, b)
            del self.fragments[max(a, b)]
            del self.fragments[min(a, b)]
            self.fragments.append(r)
            self.len -= 1

        return ''.join(self.fragments)

if __name__ == '__main__':
    # print commonOverlapIndexOf('abbbc', 'bbbd')
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            solver = Solver(line.strip().split(';'))
            print solver.solve()