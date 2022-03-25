import sys

'''
https://www.acmicpc.net/problem/2447
별 찍기 - 10
'''


def append_stars(n):
    if n == 1:
        return ["*"]

    stars = append_stars(n//3)
    list = []
    for i in stars:
        list.append(i * 3)
    for i in stars:
        list.append(i + ' '*(n//3) + i)
    for i in stars:
        list.append(i * 3)

    return list


def baek():
    n = int(input())
    print('\n'.join(append_stars(n)))

