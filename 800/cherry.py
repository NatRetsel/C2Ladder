"""
    Given a list of integer strings, find the value of the max(i,j,...,n) * min(i,j,...,n) over all pairs

    Strategy
    1.) Brute force (TLE)
        - nested for loop, find the max and min elements bounded by two indices, shortlist max product

    2.) Consider only adjacent pairs
        - we want the max of max*min, so we want both values to be as large as possible
        - extending beyond 2 adjacent elements yield the following
            - increase max but decrease min
            - keep both same
        - in the example [3,2,3,1]
            - [3,2] = 3*2
            - [2,3] = 2*3
            - [3,1] = 3
        - When we went with the brute force
            - [3,2] = 3*2      compare this to the one immediate below, extending keeps the max and min the same;
                                if the next element were to be say [4], then the min gets reduced to 2, it will  be
                                local maxima but because of the 2 included, any subsequent higher numbers extended will
                                not benefit the min
            - [3,2,3] = 3*2    compare this and the one immediate below
            - [3,2,3,1] = 3*1  extending by 1 introduces a new min, worsening the result
            - [2,3] = 2*3
            - [2,3,1] = 2*3
            - [3,1] = 3*1

        - [3,2,3,4]

"""

from typing import List

def solve()->None:
    length:int = int(input())
    num_list:List[int] = [int(num) for num in input().split(" ")]
    res: int = 0
    for i in range(length-1):
        res = max(res, num_list[i]*num_list[i+1])

    print(res)
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()

if __name__ == '__main__':
    main()
