"""
    Given an array of unique integers > 0, find the minimum number of steps required to remove the minimum
    and maximum numbers in the array.

    At each step, we are only allowed to remove leftmost or right most element

    Strategy
    1.) Two pointers
        - find index of both smallest and largest element and compute their distance to both edge
        - proceed to remove the side closest to the edge of the two, advance corresponding edge pointer
        - repeat until both are removed
"""
from typing import List

def solve(nums:List[int], length:int, min_pos:int, max_pos:int)->None:
    left:int = 0
    right:int = length-1
    res:int = 0
    # Assume removing minimum num first
    idx_remove_first:int = min_pos
    first_dist_to_left:int = min_pos - left
    first_dist_to_right:int = right - min_pos

    idx_remove_second:int = max_pos
    second_dist_to_left:int = max_pos - left
    second_dist_to_right:int = right - max_pos

    if (min(first_dist_to_left, first_dist_to_right) > min(second_dist_to_left,second_dist_to_right)):
        # switch order
        idx_remove_first, idx_remove_second = idx_remove_second, idx_remove_first
        first_dist_to_left, second_dist_to_left = second_dist_to_left, first_dist_to_left
        first_dist_to_right, second_dist_to_right = second_dist_to_right, first_dist_to_right

    # remove first num
    if (first_dist_to_left < first_dist_to_right):
        # remove from left if distance to left edge is shorter
        res += first_dist_to_left+1
        left = idx_remove_first+1
    else:
        # remove from right if distance to right edge is shorter
        res += first_dist_to_right+1
        right = (idx_remove_first-1)

    # remove second num
    second_dist_to_left:int = idx_remove_second - left
    second_dist_to_right:int = right - idx_remove_second
    if (second_dist_to_left < second_dist_to_right):
        # remove from left if distance to left edge is shorter
        res += second_dist_to_left+1
    else:
        # remove from right if distance to right edge is shorter
        res += second_dist_to_right+1

    print(res)
    return

def main() -> None:
    testcases:int = int(input())
    nums:List[int] = []
    length: int = 0
    max_pos:int = 0
    min_pos:int = 0
    for i in range(testcases):
        length = int(input())
        nums = [int(num) for num in input().split(" ")]
        for j in range(length):
            num = nums[j]
            if (num == 1):
                min_pos = j
            if (num == length):
                max_pos = j
        solve(nums, length, min_pos, max_pos)
        nums = []
        length = 0
        min_pos = 0
        max_pos = 0
    return

if __name__ == '__main__':
    main()
