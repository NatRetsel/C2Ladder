/*
 * Polycarp must pay exactly n burles at the checkout. He has coins of two nominal values: 1 and 2. Polycarp
 * likes both kinds of coins equally. So he doesn't want to pay with more coins of one type than with the other.
 *
 * Therefore Polycarp wants to minimize the difference between the counts of coins of 1 burle and 2 burle being used.
 * Help him by determining two non-negative integer values c1 and c2 which are the number of coins of 1 burle and 2 burle
 * respectively so that the total value of the number of coins is exactly n, and the absolute difference between
 * c1 and c2 is minimized.
 *
 * Input:
 * first line number of test case
 * each test case consists of one line, this line contains one integer - the number of burles to be paid by Polycarp
 *
 * Output:
 * Separate line for each test case, with c1 followed by c2, separated by a space. If there are multiple optimal
 * solutions, print any one.
 *
 * Strategy
 * - Divide by 3, Note any remainder, if remainder 1, increment c1, if remainder 2, increment c2
 */

#include<iostream>

void solve(int payable){
    int c1 {payable/3};
    int remainder {payable%3};
    switch (remainder){
        case 1:
            std::cout << c1+1<<" "<<c1<<std::endl;
            break;
        case 2:
            std::cout << c1<<" "<<c1+1<<std::endl;
            break;
        default:
            std::cout << c1<<" "<<c1<<std::endl;
    }
    return;
}

int main(){
    int testCases {0};
    int payable {0};
    std::cin >> testCases;
    for (int i=0; i<testCases; i++){
        std::cin >> payable;
        solve(payable);
    }
    return 0;
}
