import sys

'''
https://www.acmicpc.net/problem/2908
상수
22.02.05
'''

def baek():
    N, M = map(int, input().split())

    N_list = list(str(N))
    N_list.reverse()
    reverse_N = int(''.join(N_list))
    # print(reverse_N)

    M_list = list(str(M))
    M_list.reverse()
    reverse_M = int(''.join(M_list))
    # print(reverse_M)

    # if(reverse_N > reverse_M):
    #     print(reverse_N)
    # else:
    #     print(reverse_M)

    print(max(reverse_N, reverse_M))
