#!/bin/env python
# encoding: utf-8

"""
left_rotation.py

A left rotation operation on an array of size n shifts each of the array's
elements 1 unit to the left. For example, if 2 left rotations are performed on
array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array of n integers and a number, d, perform d left rotations
on the array. Then print the updated array as a single line of space-separated integers.

Created by Michel Betancourt on 2017.
Copyright (c) 2017 ACT. All rights reserved.
"""


def main():
    rot = int(input().strip().split(' ')[1])
    arr = input().strip().split(' ')
    arr = arr[rot:] + arr[:rot]
    print(' '.join(arr))


if __name__ == '__main__':
    main()
