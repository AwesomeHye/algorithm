import sys

'''
https://www.acmicpc.net/problem/1152
단어의 개수
22.02.05
'''

def baek():
    # s = list(input().strip().split(" "))
    # if s[0] == '':
    #     print(0)
    # else:
    #     print(len(s))
    print(len(input().split())) # None (the default value) means split according to any whitespace, and discard empty strings from the result
