__author__ = 'zadoev@gmail.com'


import timeit


print "format: {}".format(
    timeit.timeit(lambda: "{0:b}".format(123123123))
)

print "bin: {}".format(
    timeit.timeit(lambda: bin(123123123)[2:])
)