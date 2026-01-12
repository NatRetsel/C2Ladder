"""
    Given an array of integers, output the index containing the number that is not like the rest.
    It is guaranteed to have a solution.

    Strategy
    1. Two pointers
        - once we find two mismatch indices, we compare the element with another index to find out the result
"""
from typing import List

def solve()->None:
    num_1_idx:int = 0
    num_2_idx:int = -1
    num_1_count: int = 0
    num_2_count: int = 0
    res:int = -1
    length:int = int(input())
    nums:List[int] = [int(num) for num in input().split(" ")]
    for i in range(length):
        if (nums[i] == nums[num_1_idx]):
            num_1_count += 1
        else:
            if (num_2_idx == -1):
                num_2_idx = i
            num_2_count += 1

        if (num_1_count >= 2 and num_2_count > 0):
            res = num_2_idx
            break

        if (num_2_count >= 2 and num_1_count > 0):
            res = num_1_idx
            break


    print(res+1)


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()


if __name__ == '__main__':
    main()
