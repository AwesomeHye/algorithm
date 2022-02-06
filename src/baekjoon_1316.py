import sys

'''
https://www.acmicpc.net/problem/1316
그룹 단어 체커
22.02.06
'''

def baek():
    n = int(input())
    words = list(input() for _ in range(n))

    cnt = n
    for word in words:
        for ch in word:
            ch_dup_cnt = word.count(ch)
            if ch_dup_cnt > 1:
                ch_group = ch * ch_dup_cnt
                if ch_group not in word:
                    cnt -= 1
                    break

    print(cnt)


