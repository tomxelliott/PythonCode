import itertools
first = raw_input().split()
second = raw_input().split()
for r in itertools.product(first, second):
    print '({0}, {1})'.format(int(r[0]), int(r[1])), 
