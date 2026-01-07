"""
    Given an integer num, find the number of interesting integers between 1 and num inclusive
    a number x is interesting if the sum of its digits is greater than the sum of the digits of x+1

    Strategy
    1.) brute force + hashmap (TLE)
        - loop for 1 till num, compute digit sum for each number and number+1 and shortlist interesting num
    2.) Observation
        - first interesting number is 9
        - Next is 19 (9*2 + 1)
        - Next is 29 (9*3 + 2)
        - 39 (9*4 + 3)
        ...
        99 (9*11 or (9*10 + 9))
        109
        119
        We can loop from 9 to n, increment in amounts of 10
        (9*n + (n-1)) where n tells us how many interesting num

        num = 3; (9n + n - 1) = 3; (10n - 1) = 3; 10n = 4; n = 0.25 ~ 0
        num = 10; 10n-1 = 10; 10n = 11; n = 1.1 ~ 1
        num = 34; 10n-1 = 34; 10n = 35; n = 3.5 ~ 3
        num = 880055535; 10n = 880055536; n =
"""



def solve()->None:
    num:int = int(input())
    print(int((num+1)/10))
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()

if __name__ == '__main__':
    main()
