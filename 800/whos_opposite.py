"""
    Given 3 integers a, b, c where they supposed to be part of even number of points on a circle.
    a is supposed to stare at b. Find the number supposed to stare a c. -1 if no such circle exist

    We know circle has even number of points
    For some point x on the circle, the number of points adjacent clockwise to reach its opposite point y is
    (total num points / 2) - 1.
    - From here we can work out the number of points of this supposed circle fulfilling a and b
    -

    6 2 4
    - num points; 3+1 = (total_num_points / 2); num_points = 8
    - for a circle of 8 points, there are (8/2)-1 = 3 points between 4 and its opposite point; 8, fufills

    2 3 1
    - num points; 0+1 = (total_num_points/2); num_points = 2
    - for a circle with 2 points, there are (2/2)-1 = 0 points between 3 and its opposite point; impossible

    2 4 10
    - num points; 1+1 = (t/2); num points = 4
    - for a circle with 4 points, there are (4/2)-1 = 1 point between 10 and its opposite point; impossible

    5 3 4
    - num points; 1+1 - (t/2); num points = 4
    - for a circle with 4 points, there are 1 point between 5 and its opposite point



"""
from typing import List

def solve()->None:
    points:List[int] = [int(num) for num in input().split(" ")]
    gap_required:int = abs(points[0] - points[1])-1
    total_points:int = (gap_required+1)*2
    if (max(points) > total_points):
        print(-1)
    else:
        res = points[2]+gap_required+1
        if res > total_points:
            print(res%total_points)
        else:
            print(res)

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()

if __name__ == '__main__':
    main()
