#include <iostream>
#include <algorithm>
#include<vector>
/* Construct a Rectangle
 * Given 3 sticks of lengths l1, l2, l3, determine if it is possible to break any one of them into two sticks
 * such that now the four sticks are able to form a rectangle (squares included).
 *
 * Strategy
 * - Want to break the longest of the bunch if there is a distinct longest candidate, else we break the smallest
 * - Ways to break it:
 * - - case 1: into copies of the two other sticks respectively (if l1 is largest, then l1 = l2 + l3)
 * - - case 2: break smallest into two distinct equal pieces (if l1 and l2 same length, break l3 cleanly in half)
 * - If we are not able to do any of it, then it is impossible
 */


void solve(){
    std::vector<int>lengths(3,0);
    std::cin >> lengths[0] >> lengths [1] >> lengths [2];
    std::sort(lengths.begin(), lengths.end());
    bool solvable {false};
    if (lengths[1] == lengths[2]) {
        if (lengths[0] % 2 == 0) solvable = true;
    }else if (lengths[0] == lengths[1]){
        if (lengths[2] % 2 == 0) solvable = true;
    }else if (lengths[0] + lengths[1] == lengths[2]){
        solvable = true;
    }

    if (solvable) std::cout << "YES";
    else std::cout << "NO";
    std::cout << std::endl;
    return;
}

int main(){
    int numTestCases {0};
    std::cin >> numTestCases;
    for (int i=0; i<numTestCases; i++) solve();

    return 0;
}
