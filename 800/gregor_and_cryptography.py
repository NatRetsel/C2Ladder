"""
    Given a prime number, find 2 numbers a and b where 2<=a<b<=P such that P mod a == P mod b
"""

def solve()->None:
    prime:int = int(input())
    for num in range(prime, 3,-1):
        if (num%2 == 0):
            print('{} {}'.format(2,num))
            break
    return

def main()->None:
    testcases:int = int(input())
    for i in range(testcases):
        solve()
    return


if __name__ == '__main__':
    main()
