"""
Name: Emir Lejlic
Date: 19.07.16

This is a scribble script used to test code.
"""

import numpy as np
from collections import Counter


def add_two(a, b):
    """Test function"""
    return a + b

if False:
    # Testing the Counter module
    print add_two(4, 5)
    c = Counter(np.arange(6))
    print c
    c = Counter(['Emir', 'Idunn', 'Emir'])
    print c

if True:
    # Testing strip
    test = 'hello\n'

    test = test.strip()
    print test
