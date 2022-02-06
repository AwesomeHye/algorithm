import sys

'''
https://www.acmicpc.net/problem/1065
한수
'''


def is_hansu(num: int):
    s = list(map(int, str(num)))
    prev_gap = -1
    for i in range(1, len(s)):
        gap = s[i] - s[i - 1]
        if i != 1 and prev_gap != gap:
            return False
        prev_gap = gap

    return True


def baek():
    n = int(sys.stdin.readline())
    count = 0
    for num in range(1, n + 1):
        if is_hansu(num):
            count += 1
    print(count)
