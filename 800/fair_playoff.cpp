/*
 * Four players participate in the playoff tournament. The tournament is held according to the following scheme
 * first player will play with the second, the third will play with the fourth. The winners of the pairs
 * playoffs in the finals.
 *
 * Skill levels are pairwise different. The tournament is called fair if the two players with the highest skills
 * meet in the finals.
 *
 * Determine whether the given tournament is fair.
 *
 * Input:
 * - first line is the number of test cases
 * - a single line of test case of 4 integers
 *
 * Output:
 * - "YES" if fair
 * - "NO" if not fair
 *
 * Strategy
 * - if the max of one pair is less than the min of the other pair, output "NO"
 *
 */


#include<iostream>
#include <utility>

 void solve(){
     int minPair1 {-1};
     int maxPair1 {-1};
     int minPair2 {-1};
     int maxPair2 {-1};

     std::cin >> minPair1;
     std::cin >> maxPair1;
     if (minPair1 > maxPair1) std::swap(minPair1,maxPair1);
     std::cin >> minPair2;
     std::cin >> maxPair2;
     if (minPair2 > maxPair2) std::swap(minPair2,maxPair2);
     if (maxPair1 < minPair2 || maxPair2 < minPair1) std::cout << "NO" << std::endl;
     else std::cout<<"YES"<<std::endl;
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
