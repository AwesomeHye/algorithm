import sys

'''
https://www.acmicpc.net/problem/11720
숫자의 합
'''


def baek():
    n = int(sys.stdin.readline())
    num_list = list(map(int, str(input())))

    print(sum(num_list))
