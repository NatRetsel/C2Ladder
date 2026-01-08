"""
    Given a string, determine the maximum number of characters that can be colored red after performing
    operation.

    Operation:
        - Each character can only be painted either red or green
        - for the same two character, it must be colored differently
        - the number of reds must match the number of greens


    Strategy
    1.) Hashmap count
        - map tells us the number of distinct characters and how many copies of it are in the string
        - for characters with >= 2 count, only one count of red paint per distinct character
        - for the rest of the distinct characters, half of it will be coloured red
        - edge case
            - string lenght 1, none can be painted

"""

from typing import Dict

def solve()->None:
    word:str = input()
    res:int = 0
    if len(word) > 1:
        cnt:Dict[str,int] = {}
        single_chars:int = 0
        for ch in word:
            if ch not in cnt.keys():
                cnt[ch] = 0
            cnt[ch] += 1

        for ch in cnt.keys():
            if cnt[ch] >= 2:
                res += 1
            else:
                single_chars += 1

        res += int(single_chars/2)

    print(res)

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()

if __name__ == '__main__':
    main()
