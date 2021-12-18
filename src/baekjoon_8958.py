"""
https://www.acmicpc.net/problem/8958
OX퀴즈
"""

import sys


def baek():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        answers = input()
        score = 0
        count = 0
        for answer in answers:
            if answer == 'O':
                count += 1
                score += count
            else:
                count = 0
        print(score)
