import random
def lottery():
    for i in xrange(6):
        yield random.randint(1, 40)
    yield random.randint(1, 10)

for randr in lottery():
    print "The next number is... %d" % randr
