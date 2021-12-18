import sys

'''
https://www.acmicpc.net/problem/3052
나머지
'''


def baek():
    num_list = [int(sys.stdin.readline()) for _ in range(10)]
    rest = set()
    for num in num_list:
        rest.add(num % 42)
    print(len(rest))
