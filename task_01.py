#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 01"""

def xfibo(count):
    """Fibonacci sequence function.

    Args:
        count (int): chosen number.

    Return:
        a generator object fibonacci sequence location.

    Example:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3

        >>> xfibo(5)
        <generator object xfibo at 0x022ECD00>
    """

    iterations = 0
    lastnum = 0
    curnum = 1
    while iterations < count:
        yield lastnum
        lastnum, curnum = curnum, curnum + lastnum
        iterations += 1
