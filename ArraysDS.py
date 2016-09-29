#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# Challenge located at: https://www.hackerrank.com/challenges/arrays-ds
# My solution below
arr = arr[::-1]
temp = ""
for _ in arr:
    temp += str(_)
    temp += " "
print(temp)