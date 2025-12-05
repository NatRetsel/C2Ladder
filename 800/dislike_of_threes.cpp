/*
 * Polycarp doesn't like integers that are divisible by 3 or end with digit 3 or both.
 * Polycarp starts to write out the positive integers which he likes.
 * Output the kth element of this sequence (numbered from 1)
 *
 * Input:
 * - first line contains the number of test cases
 * - Each test case consists of one line containing one integer k [1,1000]
 *
 * Output:
 * - one integer, the kth element of the sequence
 *
 * Strategy
 * - Generate the entire k sequences, store it in an array
 * - Lookup values
 */

#include<iostream>
#include<vector>

void genSequence(std::vector<int>&sequence, int k){
    int currNum {1};
    for (int i=1; i<=1000; i++){
        while (currNum % 3 == 0 || currNum % 10 == 3) currNum++;
        sequence[i-1] = currNum;
        currNum++;
    }
    return;
}

void solve(std::vector<int>&seq){
    int idx {0};
    std::cin >> idx;
    std::cout << seq[idx-1] << std::endl;
    return;
}

int main(){
    std::vector<int>seq(1000,1);
    genSequence(seq, 1000);
    int numTestCases {0};
    std::cin >> numTestCases;
    for (int i=0; i<numTestCases; i++) solve(seq);
    return 0;
}
