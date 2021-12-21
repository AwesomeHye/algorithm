import sys

'''
https://www.acmicpc.net/problem/1157
단어 공부
'''

# todo 디버깅!! 값 틀림
def baek():
    s_list = list(input())
    ignore_s_list = [s if ord(s) < 97 else chr(ord(s)-32) for s in s_list]
    print(ignore_s_list)

    count_dic = {}
    for _ in ignore_s_list:
        if _ in count_dic.keys():
            count_dic[_] += 1
        else:
            count_dic[_] = 1

    sorted_count_dic = sorted(count_dic.items(), key=lambda dic: dic[1], reverse=True)

    symbol = '?'
    first_value = 0
    idx = 0
    for key, value in sorted_count_dic:
        if idx == 0:
            symbol = key
            first_value = value
            continue

        if idx == 1 and value == first_value:
            symbol = '?'
            break

        idx += 1

    print(symbol)

