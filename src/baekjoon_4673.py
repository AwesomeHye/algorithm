import sys

'''
https://www.acmicpc.net/problem/4673
셀프 넘버
30m
'''

LIMIT = 10000


def baek():
    # candidates = [_ + 1 for _ in range(LIMIT)]
    candidates = set(range(1, LIMIT+1))
    answers = set()
    for n in range(LIMIT):
        recursive_d(n, answers)

    for _ in sorted(candidates-answers):
        print(_)


def recursive_d(n: int, answers):
    if n > LIMIT:
        return

    n = d(n)
    answers.add(n)
    # if n in candidates:
    #     candidates.remove(n)


def d(n: int) -> int:
    # sum = n
    # n_len = len(str(n))
    # for _ in range(n_len):
    #     digit = n % 10 ** (_ + 1)
    #     if _ != 0:
    #         digit = digit // 10 ** _
    #     sum += digit
    # return sum
    return n + sum(list(map(int, str(n))))
