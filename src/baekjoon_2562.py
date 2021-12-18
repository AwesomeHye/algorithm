import sys

'''
https://www.acmicpc.net/problem/2562
최댓값
'''


def baek():
    num_list = [int(sys.stdin.readline()) for _ in range(9)]
    max_num = max(num_list)
    print(max_num)
    print(num_list.index(max_num)+1)
