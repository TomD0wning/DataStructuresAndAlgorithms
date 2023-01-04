#! /usr/bin/env python3

import collections

def natural_numbers():
    print(sum(_ for _ in range(0, 1000) if(_ % 3 == 0 or _ % 5 == 0)))


def valid_parentheses(input):
    count = [0]
    [count.append(1) if x is '(' else count.pop()
     if x is ')' and count != [] else '' for x in input]
    return len(count) == 1


def hashtag_gen(s):
    result = s.replace(" ", "")
    if(len(result) > 139 or len(result) == 0):
        return False
    return f"#{result.title()}"


def first_non_repeating_letter(s):
    res = collections.Counter(s)
    return min(res, key=res.get)


def offset_weights(s):
    lst = list(s.split(" "))
    result = []
    for x in lst:
        result.append((x, sum(int(i) for i in x)))
    return [n[0] for n in sorted(result, key=lambda s: s[1])]


def ends_with(s: str, e: str):
    return s.endswith(e)
