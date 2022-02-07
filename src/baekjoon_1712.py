import sys

'''
https://www.acmicpc.net/problem/1712
손익분기점
22.02.07
'''

def baek():
    A, B, C = map(int, input().split())
    # print(A, B, C)

    sales_cnt = -1
    if C > B:
        sales_cnt = int(A / (C - B) + 1)

    print(sales_cnt)
