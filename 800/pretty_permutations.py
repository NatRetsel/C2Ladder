"""
    Given consecutive sequence from 1 to n, output the space separated sequence of such that every element
    is not in their previous location and their combined movement is minimized

    Strategy
    1.) if n is even, swap the positions of element with the next, skip the next element.
    2.) if n is odd, after doing 1, swap positions of the last 2


"""
from typing import List

def solve()->None:
    n:int = int(input())
    nums:List[int] = [num for num in range(1,n+1)]
    for i in range(0,n-1,2):
        nums[i],nums[i+1] = nums[i+1],nums[i]
    if (n%2 != 0):
        nums[len(nums)-1], nums[len(nums)-2] = nums[len(nums)-2],nums[len(nums)-1]
    for num in nums:
        print(num,end=" ")
    print("")
    return

def main():
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
