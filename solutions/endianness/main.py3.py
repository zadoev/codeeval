__author__ = 'zadoev@gmail.com'
"""
Write a program which prints the endianness of the system.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the endianness, wheather it is LittleEndian or BigEndian.

For example:

BigEndian
"""

import sys

if __name__ == '__main__':
    print('{}Endian'.format(sys.byteorder.capitalize()))
