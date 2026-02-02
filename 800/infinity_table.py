"""
    given an integer k, output the space separated row, col indices on where the integer will be in the inifite
    square grid filled according to the algorithm:
        - Select leftmost non-filled cell and fill it.
        - While the left neighbor of the last filled cell is filled, we go down and fill the next cell until
        the last filled cell has a non-filled neighbor to the left.
        - After that, fill right to left until we reach the first column (1 indexed).
        - Then repeat


    Strategy
    1.) Simulate till n O(n2)
        - given an integer n, we can simulate the filling process then return the row, col index when we reached n

    2.) Math
        - notice in the diagram that the first column of each row (1 indexed) follows index squared
        - And that will be the largest number and if we trace exactly (index) times to the right, then (index) times
        to the top, we get sequentially decreasing order
        - So we can first find which row (thus column) is the supplied integer in by x = ceil(sqrt(n))
            - then we know the largest number in this outer perimeter where n is in is x squared
            - if x squared - n > x-1, then n is along the rightmost outer perimeter column else it resides in the
           bottomost row.
                - if x squared - n > x-1,
                    - column value =  x
                    - row value = n - (x*x- ((x-1)*(x-1)+1)) + 1
                - else
                    - row value = x
                    - column value = (x*x) - n + 1
"""
import math

def solve()->None:
    n:int = int(input())
    x:int = math.ceil(math.sqrt(n))
    row:int = 0
    col:int = 0
    if ((x*x - n) > (x-1)):
       col = x
       row = n - ((x-1)*(x-1))
    else:
        row = x
        col = x*x - n + 1
    print(f"{row} {col}")
    return


def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == "__main__":
    main()
