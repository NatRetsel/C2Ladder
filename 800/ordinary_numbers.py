"""
    Given an integer n >= 1, output the number of integers that are ordinary.
    A number is ordinary if the decimal notation of its digits are the same. When it contains only
    one digit then the number has to be ordinary

    Strategy
    1.) Cache previous results to avoid multiple generation
        - know that for each new increment to its significant digit, the number of ordinary num increases by 9
        - Determine how many places the number goes to, multiply that by 11 to get the maximum ordinary number
        available for that place
        - subtract this number by (9 - digit at max place)
        - if given number is smaller than the ordinary number we would get by repeating the max place digit, subtract
        another one
"""


def solve()->None:
    num:int = int(input())
    num_places:int = 0
    first_digit:int = 0
    res:int = 0

    num_copy:int = num
    while(int(num_copy/10) > 0):
        num_copy = int(num_copy / 10)
        num_places += 1
    # print("num places: {}".format(num_places))
    first_digit = int(num / (10**num_places))
    # print("first digit: {}".format(first_digit))
    max_ordinary_num = (num_places+1) * 9
    # print("max o num {}".format(max_ordinary_num))
    res = max_ordinary_num - (9-first_digit)

    first_digit_o_num = int(str(first_digit) * (num_places+1))
    # print("first digit o num: {}".format(first_digit_o_num))

    if (num < first_digit_o_num):
        res -= 1

    print(res)

    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return


if __name__ == '__main__':
    main()
