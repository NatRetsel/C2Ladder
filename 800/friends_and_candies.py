"""
    Given a stream of integers, determine the minimum number of positions such that the redistribution of
    the sum can bring equal distribution throughout the stream
"""

from typing import List

def solve() -> None:
    length:int = int(input())
    num_list:List[int] = [int(num) for num in input().split(" ")]
    total:int = sum(num_list)
    res: int = 0
    if (total % length != 0):
        res = -1
    elif (total % length == 0):
        eq_weight:int = int(total / length)
        num_surplus:int = 0

        for num in num_list:
            if num > eq_weight:
                num_surplus += 1

        res = num_surplus
    print(res)
    return

def main() -> None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()


if __name__ == '__main__':
    main()
