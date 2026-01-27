"""
    Given the size of the chessboard, positions of enemy pawn in the first row and positions of gregor's pawn
    in string format "0" denotes empty slot in the position and "1" denotes pawn occupying that position.

    Determine the maximum number of gregor's pawn that can reach and occupy enemy pawns position

    Pawn can move i-1,j if nothing is blocking
    Pawn can move i-1,j+1 or i-1,j-1 if enemy pawn is occupying there, and enemy pawn is then removed as a result

    Strategy
    - Greedy
        - if path ahead is empty, we advance
        - if path ahead is blocked and there is a pawn available to capture on either side, we capture.
            - since we iterate left to right, we prioritise left then right
        - edge cases, no pawns to begin with

    - backtracking
        - for each index we can choose the following steps if we have a pawn
            if path ahead is empty, we advance
            OR
            if there is a pawn available to capture on the left, we capture
            OR
            capture pawn on the right


"""
from typing import List



def solve()->None:
    board_size: int = int(input())
    target_positions:List[str] = [ch for ch in input()]
    starting_positions:List[str] = [ch for ch in input()]
    res:int = 0

    for i in range(board_size):
        if starting_positions[i] == "1":
            if target_positions[i] == "0":
                res += 1
            elif i-1 >= 0 and target_positions[i-1] == "1":
                res += 1
                target_positions[i-1] = "2"
            elif i+1 < board_size and target_positions[i+1] == "1":
                res += 1
                target_positions[i+1] = "2"
    print(res)
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
