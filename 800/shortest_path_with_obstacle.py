"""
    Given the 2D coordinates of 3 positions A, B, and F. Find the shortest distance moving from A to B without
   touching F.
   Constraints:
       infinite grid
       permitted moves are up down left right

    The shortest distance between two points on a grid where the permitted moves are only up down left and right
    can be computed using the manhattan distance
    |x1-x2| + |y1-y2|

    Concerns about F affecting out manhattan distance are only relevant if it lie in the same row or column as
    our starting position, and A and B are on that same row or column and F is between A and B to which we need to add 2
"""

from typing import List

def solve()->None:
    # Read coordinates
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())

    # Calculate Manhattan distance
    dist = abs(xa - xb) + abs(ya - yb)

    # Check if F blocks the shortest path
    if xa == xb == xf:  # Same column
        # F must be between A and B
        if min(ya, yb) < yf < max(ya, yb):
            dist += 2
    elif ya == yb == yf:  # Same row
        # F must be between A and B
        if min(xa, xb) < xf < max(xa, xb):
            dist += 2
    print(dist)
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        input()
        solve()
    return

if __name__ == '__main__':
    main()
