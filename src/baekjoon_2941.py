import sys

'''
https://www.acmicpc.net/problem/2941
크로아티아 알파벳
22.02.06
'''

def baek():
    # croatias = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    # inputs = input()

    # cnt = 0
    # for croatia in croatias:
    #     cnt += inputs.count(croatia)
    #     inputs = inputs.replace(croatia, '_')

    # cnt += len(inputs.replace('_', ''))
    # print(cnt)
    word = input()
    length = len(word)
    cro_apbt = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for i in cro_apbt:
        if i in word:
            tmp = word.count(i)
            length -= tmp
    print(length)