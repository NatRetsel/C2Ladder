"""
    Given an integer n, find the maximum int k such that
    n & (n-1) & (n-2) & ... & k = 0

    E.g.
        n = 2, k = 1
        binary
            1 0
        &     1
        --------
            0 0

        n = 5
        binary
            1 0 1
        &   1 0 0
            -----
            1 0 0
        &   0 1 1
            -----
            0 0 0


    Strategy
    1.) brute force (TLE)
        - loop down from n to 1
        - compute consecutive ands, return the first result that yields 0

    2.) Observation
        - Let's look at what happen when we do bitwise and on consecutive numbers
        5: 101
        4: 100
        3: 011
        2: 010
        1: 001

        From 5 to 4, right most bit is set to 0 with consecutive AND, all that's left is turning left most bit to 0
        From 4 to 3, left most bit is turned off
        From 3 to 2, right most bit is set to 0, we need to set leftmost bit to 0
        From 2 to 1, left most bit it set to 0

        17: 10001 2^4 + 1
        16: 10000 2^4
        15: 01111 2^4-1 or 2^3 + 2^2 + 2^1 + 2^0
        14: 01110 2^4-2 or 2^3 + 2^2 + 2^1
        13: 01101
        12: 01100
        11: 01001
        10: 01000
        09: 00111

        17 to 16: rightmost bit removed, need to remove leftmost bit
        16 to 15: leftmost bit removed
        15 to 14: rightmost bit removed, need to remove all left bits
        14 to 13: right bit removed, need more
        ...
        10 to 09: all bits removed

        Pattern:
            Given n, we need to find the nearest number with the leftmost significant digit removed
            - first find the position of the largest significant bit occupied by n
                - count number of right shifts until n becomes 0
                - return 2^n - 1

"""

def solve()->None:
    num:int = int(input())
    num_copy:int = num
    n:int = -1
    while (num_copy > 0):
        n += 1
        num_copy >>= 1
    print((2**n) - 1)


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()

if __name__ == '__main__':
    main()
