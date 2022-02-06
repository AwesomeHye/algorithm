"""
https://www.acmicpc.net/problem/2675
문자열 반복
"""

import sys


def baek():
    input = sys.stdin.readline

    for _ in range(int(input())):
        R, S = list(input().split())

        R = int(R)
        for ch in S:
            print(ch*R, end='')

        print('')