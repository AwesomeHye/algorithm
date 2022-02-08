import sys

'''
https://www.acmicpc.net/problem/10872
팩토리얼
22.02.08
'''


def fac(n):
    if n == 0:
        return 1

    return n * fac(n - 1)


def baek():
    n = int(input())
    print(fac(n))
