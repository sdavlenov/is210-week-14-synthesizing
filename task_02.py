#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 02"""

import task_01


def fibo(count):
    """Function returns fibonacci generator as a list.

    Args:
        count (int): number to generate sequence.

    Return:
        list of fibonacci sequence numbers up to given number.

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """

    iterator = 0
    fib_list = [num for num in task_01.xfibo(count)]
    while iterator < count:
        iterator += 1
    return fib_list
