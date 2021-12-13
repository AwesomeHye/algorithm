import sys

'''
https://www.acmicpc.net/problem/1110
더하기 사이클
'''
n = int(sys.stdin.readline())  # 68
next_n = n
cycle = 0
while cycle == 0 or (cycle != 0 and n != next_n):  # 처음 시도거나 처음시도가 아니고 비교 수가 다르면
    temp = next_n // 10 + next_n % 10  # 6+8=14
    next_n = (next_n % 10) * 10 + temp % 10  # 60+4=64
    cycle += 1
print(cycle)


