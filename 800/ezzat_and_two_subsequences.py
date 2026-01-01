"""
    Given a sequence of numbers, output the maximum average sum attainable when splitting the sequence
    into 2 subsequences.

    Strategy
    - The maximum value stays alone in its subsequence
    - The rest in its own subsequence

"""

from typing import List


def solve(seq_length:int, seq:List[int], max_num:float) -> None:
    subseq_sum_one:int = 0
    subseq_one_length:int = 0
    subseq_sum_two:int = 0


    for num in seq:
        if num == int(max_num) and subseq_one_length == 0:
            subseq_sum_one = int(max_num)
            subseq_one_length = 1
        else:
            subseq_sum_two += num

    print(subseq_sum_one + (subseq_sum_two/(seq_length-1)))
    return


def main():
    num_testcases: int = 0
    seq_length: int = 0
    seq: List[int] = []
    max_num: float = -float('inf')

    num_testcases = int(input())
    for i in range(num_testcases):
        seq_length = int(input())
        str_seq:List[str] = input().split(" ")
        for j in range(seq_length):
            seq.append(int(str_seq[j]))
            max_num = max(max_num, seq[-1])
        solve(seq_length, seq, max_num)
        max_num = -float('inf')
        seq = []

    return


if __name__ == '__main__':
    main()
