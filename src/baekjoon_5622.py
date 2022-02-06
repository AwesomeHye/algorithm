import sys

'''
https://www.acmicpc.net/problem/5622
다이얼
22.02.06
'''

def baek():
    inputs = input()

    # dials = {}
    # num = 0
    # for i in range(ord('A'), ord('Z') + 1):
    #     if i <= ord('C'):
    #         num = 3
    #     elif i <= ord('F'):
    #         num = 4
    #     elif i <= ord('I'):
    #         num = 5
    #     elif i <= ord('L'):
    #         num = 6
    #     elif i <= ord('O'):
    #         num = 7
    #     elif i <= ord('S'):
    #         num = 8
    #     elif i <= ord('V'):
    #         num = 9
    #     else:
    #         num = 10
    #
    #     dials[chr(i)] = num

    time = 0
    for alphabet in inputs:
        # time += dials[alphabet]
        if alphabet in "ABC":
            time += 3
        elif alphabet in "DEF":
            time += 4
        elif alphabet in "GHI":
            time += 5
        elif alphabet in "JKL":
            time += 6
        elif alphabet in "MNO":
            time += 7
        elif alphabet in "PQRS":
            time += 8
        elif alphabet in "TUV":
            time += 9
        else:
            time += 10

    print(time)