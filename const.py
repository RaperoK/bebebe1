START = False
PAUSE = False
SAVE_PERCENT = True
LIMIT_VOL: 103
LIMIT_PERCENT: 100
LIMIT_ODD: 349
LIMIT_TIME: 45

CATEGORY = {'all': 'Все матчи', 'live': 'Онлайн матчи', 'prematch': 'Предстоящие матчи'}
FIRST_HALF = {'goal0_5': 0.5, 'goal1_5': 1.5, 'goal2_5': 2.5, 'none': 'нет'}

MONEY = {'min': 0, 'max': 10000000}
PERCENT = {'min': 0, 'max': 100}
COEFF = {'min': 1.01, 'max': 1000}
TIME1 = {'min': 0, 'max': 45}
TIME2 = {'min': 45, 'max': 90}

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