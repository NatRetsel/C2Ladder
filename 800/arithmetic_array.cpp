/*
 * An array b of length k is called good if its arithmetic mean is equal to 1 unrounded.
 * Given an integer array a of length n, in an operation, we can append a non negative integer to
 * the end of the array, what is the minimum number of operations required to make the array good?
 *
 * Input:
 * - first line contains the number of test cases
 * - first line of each test case contains n, length of array
 * - second line of each test case contains n integers
 *
 * Output:
 * - the mininum number of non-negative integers to append to the arrya for the arithmetic mean to be 1
 *
 *
 * Considerations:
 * - Positive running sum
 *  - E.g.
 *      - length 3, sum 1 (length > sum), answer 1
 *      - length 2, sum 100 (length < sum), answer 100 - 2
 * - Negative running sum
 *      - length > sum; answer is 1
 *
 * - Zero running sum
 *      - length > sum; answer is 0
 *
 *
 * Strategy
 * - Know that the arithmetic mean equals 1 when sum of numbers equal length
 * - Capture running sum and current length
 */

#include<iostream>

void solve(){
    int length {0};
    int runSum {0};
    int currNum {0};
    std::cin >> length;
    for (int i=0; i<length; i++) {
        std::cin >> currNum;
        runSum += currNum;
    }

    if (runSum > length) std::cout << runSum - length << std::endl;
    else if (runSum == length) std::cout << 0 << std::endl;
    else std::cout << 1 << std::endl;
    return;
}

int main(){
    int numTestCases {0};
    std::cin >> numTestCases;
    for (int i=0; i<numTestCases; i++){
        solve();
    }
    return 0;
}
