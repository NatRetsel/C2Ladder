#include <iostream>
#include <unordered_map>

/* Casimir's String Solitaire
 * Given a string consisting of letters 'A', 'B' and 'C' only, determine if all characters
 * can be removed by performing operations at each step.
 *
 * Operation:
 * a.) Remove one 'A' and one 'B' from arbitrary positions
 * b.) Remove one 'B' and one 'C' from arbitrary positions
 *
 * Strategy
 * - Since 2 characters are removed at once, if the string is odd length, then it is impossible
 * - Count of 'A' must match count of 'B'
 * - Count of 'B' must match count of 'C'
 * - If string only contains 2 characters, we check for respective pairing and their count
 * - If string contains all 3 characters, then count of 'A' + 'C' must equal 'B'
 */

void solve(){
    std::string word {""};
    std::cin >> word;
    if (word.length()%2==1){
        std::cout<<"NO"<<std::endl;
        return;
    }
    int countA{0}, countB{0}, countC{0};
    for (int i=0; i<word.length(); i++){
        if (word[i] == 'A') countA++;
        else if (word[i] == 'B') countB++;
        else countC++;
    }
    if (countA == 0 || countB == 0 || countC == 0){
        if (countB == 0){
            std::cout << "NO";
        } else if (countA == 0){
            if (countB == countC) std::cout << "YES";
            else std::cout<<"NO";
        }else{
            if (countA == countB) std::cout << "YES";
            else std::cout<<"NO";
        }
    }else{
        if ((countA + countC) == countB) std::cout << "YES";
        else std::cout << "NO";
    }
    std::cout<<std::endl;
    return;
}

int main(){
    int numTestCases {0};
    std::cin >> numTestCases;
    for (int i=0; i<numTestCases; i++) solve();
    return 0;
}
