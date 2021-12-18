import sys

'''
https://www.acmicpc.net/problem/10818
최소, 최대
'''


def baek():
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))

    print(min(num_list), end=' ')
    print(max(num_list))
