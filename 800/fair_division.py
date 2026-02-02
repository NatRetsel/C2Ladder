"""
    Given the number of candies and their respective weight (1 or 2). Determine if it can be
    split into two groups of equal weight. Individual candies cannot be split in half.

    - first find the target weight each group supposed to weigh assuming candies can be halved
    - if sum of weights is odd then instant NO
    - if sum of weights is even,
        - pick a combination that allows one side to achieve target weight, if impossible, NO
        - after picking one side, check the sum of the remaining weights
        OR
        - find the counts of these candies
            - number of 2's and 1's should also be even so they can be split evenly into two groups

"""




from typing import List, Dict
def solve()->None:
    num_candies:int = int(input())
    candy_weights:List[int] = [int(w) for w in input().split(" ")]
    total_weight:int = sum(candy_weights)
    if total_weight%2 != 0:
        print("NO")
        return
    target_weight:int = int(total_weight/2)
    cnt_twos:int = 0
    cnt_ones:int = 0

    for i in range(num_candies):
        if candy_weights[i] == 1:
            cnt_ones += 1
        else:
            cnt_twos += 1

    while target_weight > 0:
        if target_weight >= 2 and cnt_twos > 0:
            target_weight -= 2
            cnt_twos -= 1
        elif target_weight >= 1 and cnt_ones > 0:
            target_weight -= 1
            cnt_ones -= 1
        else:
            break

    if target_weight == 0 and (cnt_ones + 2*cnt_twos) == int(total_weight/2):
        print("YES")
        return

    print("NO")

    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return

if __name__ == '__main__':
    main()
