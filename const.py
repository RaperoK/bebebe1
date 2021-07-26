LIMIT_VOL = 103
LIMIT_PERCENT = 100
LIMIT_ODD = 349
LIMIT_TIME = 45

import numpy

def VOL_RANGE(value):
    return numpy.concatenate(
        (numpy.arange(0, 10, 1),
         [10],
         numpy.arange(10, 100, 5),
         numpy.arange(100, 1000, 50),
         numpy.arange(1000, 10000, 500),
         numpy.arange(10000, 100000, 5000),
         numpy.arange(100000, 1000000, 50000),
         [1000000, '∞', '∞']
    ))[value]

def ODD_RANGE(value):
    return round(numpy.concatenate((
        numpy.arange(1.01, 2, 0.01),
        numpy.arange(2, 3, 0.02),
        numpy.arange(3, 4, 0.05),
        numpy.arange(4, 6, 0.1),
        numpy.arange(6, 10, 0.2),
        numpy.arange(10, 20, 0.5),
        numpy.arange(20, 30, 1),
        numpy.arange(30, 50, 2),
        numpy.arange(50, 100, 5),
        numpy.arange(100, 1010, 10)
    ))[value], 2)