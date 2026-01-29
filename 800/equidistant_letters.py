"""
    Given a string of lowercase latin letters where each alphabet appears no more than twice,
    rearrange the letters such that for each pair of letters that appear exactly twice, the distance
    between the letters in the pair is the same.

    Strategy
    1.) group all pairs side by side
        - force a distance of 1 for all pairs, then place remaining 1 count characters at the back
"""

from typing import Dict,List

def solve()->None:
    s:str = input()
    ch_count:Dict[str,int] = {}
    res_list:List[str] = ["a" for i in range(len(s))]
    for ch in s:
        if ch not in ch_count.keys():
            ch_count[ch] = 0
        ch_count[ch] += 1

    f_idx:int = 0
    b_idx:int = len(s)-1
    for k,v in ch_count.items():
        if v == 2:
            res_list[f_idx], res_list[f_idx+1] = k, k
            f_idx += 2
        else:
            res_list[b_idx] = k
            b_idx -= 1

    res_str:str = "".join(ch for ch in res_list)
    print(res_str)
    return


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
