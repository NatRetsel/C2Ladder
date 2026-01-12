"""
    Given a string, determine the smallest integer k such that when selecting k characters from string
    and permute them, we are able to sort the characters in the string.

    Strategy
    1.) sort and compare
        - compare the characters of each index of the sorted string with original
        - every difference is a position we need to consider

        codeforces
        ccdeefoors
        ----------
         1  11111

"""

def solve()->None:
    length:int = int(input())
    original_str = input()
    sorted_string:str = ''.join(sorted(original_str))
    res:int = 0
    for i in range(length):
        if original_str[i] != sorted_string[i]:
            res += 1

    print(res)



def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()


if __name__ == '__main__':
    main()
