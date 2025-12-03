/*
 * Given a multiset containing 2n integers, determie if it is possible to split them into exactly n pairs
 * so that the sum of the two elements in each pair is odd
 *
 * Input
 * - first line contains integer - number of test cases
 * - first line of each test case contains n
 * - second line of each test case contains 2n integers
 *
 * Output
 * - "Yes" if possible
 * - "No" if impossible
 *
 * Strategy
 * - Count odd numbers
 * - The only time we can form odd sum is through odd + even = odd
 * - if number of odd numbers in the stream is exactly n, output "Yes", "No" otherwise
 */

#include<iostream>

void solve(){
    int n {0};
    int num {0};
    int numOdd {0};
    std::cin>>n;
    for (int i=0; i<2*n; i++){
        std::cin >> num;
        if (num % 2 == 1){
            numOdd++;
        }
    }
    if (numOdd == n) std::cout << "Yes"<<std::endl;
    else std::cout << "No"<<std::endl;
    return;
}

int main(){
    int testCases {0};
    std::cin >> testCases;

    for (int i=0; i<testCases; i++){
        solve();
    }
    return 0;
}
