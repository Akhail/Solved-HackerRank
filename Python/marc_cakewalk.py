#!/bin/env python
# encoding: utf-8

"""
    marc_cakewalk.py

    Marc loves cupcakes, but he also likes to stay fit. He eats cupcakes in one sitting,
    and each cupcake has a calorie count, After eating a cupcake with calories,
    he must walk at least 2^j * c (where is the number cupcakes he has already eaten)
    miles to maintain his weight.

    Given the individual calorie counts for each of the cupcakes, find and print a
    long integer denoting the minimum number of miles Marc must walk to maintain his
    weight. Note that he can eat the cupcakes in any order.

    Created by Michel Betancourt on 2017.
    Copyright (c) 2017 ACT. All rights reserved.
"""

def main():
    _ = int(input().strip())

    calories = input().strip().split(' ')
    calories = map(int, calories)
    calories = list(calories)
    calories.sort(reverse=True)

    total = [cal * 2**idx for idx, cal in enumerate(calories)]
    total = sum(total)

    print(total)

if __name__ == '__main__':
    main()

