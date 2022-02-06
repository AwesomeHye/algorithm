import sys

'''
https://www.acmicpc.net/problem/10809
알파벳 찾기
'''

ASCII_a = 97

def baek():
    answers = [-1 for _ in range(26)]
    asciis = list(map(ord, str(input())))

    for char in asciis:
        if answers[char - ASCII_a] == -1:
            answers[char - ASCII_a] = asciis.index(char)

    for _ in answers:
        print(_, end=' ')
