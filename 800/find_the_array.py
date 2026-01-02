"""
    Given an integer s, output the minimum possible size of a beautiful array (each element > 1) with sum of elements equal to s
    An array is beautiful if for every element, at least one criterion is fulfiled.
    * it is equal to 1
    * element - 1 exist
    * element -2 exist

    Note: We do not need the actual array - notice S = 7 and 8 has the same length of beautiful array ([1,2,4], [1,3,4])
    So we can ask in reverse, what is the largest amount a beautiful array of size n can sum to
    size 1: [1] = 1
    size 2: [1,3] = 4
    size 3: [1,3,5] = 9
    ...
    size n: n^2
    Therefore the solution is ceil(sqrt(input())); the smallest n such that n^2 >= S
"""
import math

def solve() -> None:
    s: int = int(input())
    print(math.ceil(math.sqrt(s)))
    return


def main() -> None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()


if __name__ == '__main__':
    main()
