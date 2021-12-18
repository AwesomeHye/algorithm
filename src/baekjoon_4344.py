"""
https://www.acmicpc.net/problem/4344
평균은 넘겠지
"""

import sys


def baek():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        inputs = list(map(int, input().split()))
        n = inputs[0]
        avg = sum(inputs[1:]) / n

        count = 0
        for score in inputs[1:]:
            if score > avg:
                count += 1
        print(f'{count / n * 100:.3f}%')
