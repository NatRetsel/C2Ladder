"""
    Given a ray of integers, return the minimum number of steps required to make every element equal.
    At each step we can choose some indices and increase the elements by 1

    Strategy
    1.) Simulation
        - will increase all elements until they are equal to the largest element in the array
    2.) difference between largest and smallest elements
        - the min number of steps will never be smaller than the difference between the largest and smallest
        elements
"""

from typing import List

def solve()->None:
    length:int = int(input())
    nums:List[int] = [int(num) for num in input().split(" ")]
    min_num:int = int(1e9)
    max_num: int = 0
    for i in range(length):
        min_num = min(min_num, nums[i])
        max_num = max(max_num, nums[i])
    print(max_num - min_num)
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
