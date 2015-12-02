__author__ = 'zadoev@gmail.com'
"""
Write a program to determine the lowest common ancestor of two nodes in a binary search tree. You may hardcode the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29
INPUT SAMPLE:

The first argument is a path to a file that contains two values. These values represent two nodes within the tree, one per line. E.g.:

8 52
3 29
OUTPUT SAMPLE:

Print to stdout the lowest common ancestor, one per line. Lowest means the lowest depth in the tree, not the lowest value. E.g.:

30
8

"""

import sys


class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({}, {}, {})'.format(self.value, repr(self.left), repr(self.right))


def insert(node, val):
    """
    Inserts new value into tree

    >>> tree = insert(None, 30)
    >>> tree
    Node(30, None, None)
    >>> tree = insert(tree, 8)
    >>> tree
    Node(30, Node(8, None, None), None)
    >>> tree = insert(tree, 3)
    >>> tree
    Node(30, Node(8, Node(3, None, None), None), None)
    >>> tree = insert(tree, 52)
    >>> tree
    Node(30, Node(8, Node(3, None, None), None), Node(52, None, None))
    >>> tree = insert(tree, 20)
    >>> tree
    Node(30, Node(8, Node(3, None, None), Node(20, None, None)), Node(52, None, None))

    :param node: node of tree, usually root node
    :type node: Node
    :param val: value to store in tree
    :type val: int
    :return: current node or created
    :rtype: Node
    """
    if node is None:
        node = Node()
        node.value = val
        return node

    if val <= node.value:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    return node




def solver(a, b, tree):
    """
    >>> tree = reduce(lambda a, b: insert(a, b), [30, 8, 52, 3, 20, 10, 29], None)
    >>> solver(30, 8, tree).value
    30
    >>> solver(3, 29, tree).value
    8
    >>> solver(3, 3, tree).value
    3
    >>> solver(29, 52, tree).value
    30
    >>> solver(8, 52, tree).value
    30
    >>> solver(29, 20, tree).value
    20
    >>> solver(30, 52, tree).value
    30

    :param a: one of searched values
    :type a: int
    :param b: another value to search
    :type b: int
    :param tree: node to start search, usually root node
    :type tree: Node
    :return: Found node with lowest common ancestor
    :rtype: Node
    """
    a, b = sorted((a, b))
    v = tree.value

    if a <= v and b <= v:
        if a == v or b == v:
            return tree
        return solver(a, b, tree.left)
    elif a > v and b > v:
        return solver(a, b, tree.right)
    else:
        return tree

if __name__ == '__main__':
    tree = reduce(lambda a, b: insert(a, b), [30, 8, 52, 3, 20, 10, 29], None)
    with open(sys.argv[1], 'r') as test_cases:
        for line in test_cases:
            print solver(*map(int,line.split()), tree=tree).value