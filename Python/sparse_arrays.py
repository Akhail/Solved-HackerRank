#!/bin/env python
# encoding: utf-8

"""
sparse_arrays.py

There are N strings. Each string's length is no more than 20 characters.
There are also Q queries. For each query, you are given a string, and
you need to find out how many times this string occurred previously.

Created by Michel Betancourt on 2017.
Copyright (c) 2017 ACT. All rights reserved.
"""


def main():
    number = int(input())
    words = [input().strip() for _ in range(number)]
    number = int(input())
    for _ in range(number):
        print(words.count(input().strip()))


if __name__ == '__main__':
    main()
