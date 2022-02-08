import sys

'''
https://www.acmicpc.net/problem/10870
피보나치 수 5
22.02.08
'''


def fib(n):
    # if n <= 0:
    #     return 0
    # elif n == 1:
    #     return 1
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def baek():
    n = int(input())
    print(fib(n))
