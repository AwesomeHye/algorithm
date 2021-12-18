import sys

'''
https://www.acmicpc.net/problem/2577
숫자의 개수
'''


def baek():
    mul = 1
    for _ in range(3):
        mul *= int(sys.stdin.readline())

    mul_str = str(mul)
    for i in range(10):
        print(mul_str.count(str(i)))

    # for i in range(10):
    #     count = 0
    #     for _ in mul_str:
    #         if i == int(_):
    #             count += 1
    #     print(count)
