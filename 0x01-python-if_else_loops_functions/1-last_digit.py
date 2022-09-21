#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = (abs(number) % 10) * (-1) ** (number < 0)
print('Last digit of {} is {} and is {}'.format(number, d,
      'greater than 5' if d > 5 else 'less than 6 and not 0' if d else '0'))
      