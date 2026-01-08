"""
    Given an array of integers, find the maximum number of elements that can be removed by performing
    the operation any number of times.

    Operation: from a subsequence, remove elements that are greater than the average of this subsequence

    E.g.
        [1,1,1,2,2,3]
        operation 1: choose index 0, 4, 5: average = 2 -> [1,1,1,2,2]
        operation 2: choose all index: average = 1 -> [1,1,1]
        can't perform anymore operations

    How to choose subsequence such that the max amount of elements can be removed?
    Include the smallest element to bring down the average
    - include all the max nums with a single smallest element, repeat until we are left with the smallest element
    - By this, we can always remove every element except the smallest
        - find the count of the smallest element, subtract this from the length of the array

"""
from typing import List

def solve()->None:
    length:int = int(input())
    num_list:List[int] = [int(num) for num in input().split(" ")]
    min_num:int = min(num_list)
    min_count:int = 0
    for num in num_list:
        if num == min_num:
            min_count += 1
    print(length - min_count)


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()


if __name__ == '__main__':
    main()
