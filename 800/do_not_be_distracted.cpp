/*
 * Polycarp has 26 tasks. Each task is designated by a capital letter of the latin alphabet
 * A teacher asked polycarp to solve tasks in the following way:
 * If Polycarp began to solve some task, then he must solve it to the end, without being
 * distracted by another task. After switching to another task, Polycarp cannot retun to the
 * previous task.
 *
 * Everyday he wrote down what task he solved. Now the teacher wants to know if Polycarp followed his advice.
 *
 * Help Polycarp find out if his teacher might be suspicious.
 *
 * Input:
 * - first line contains an integer t, number of test cases
 * - second line contains a string of length n, the order in which Polycarp solved the tasks
 *
 * Output:
 * - "YES" if teacher cannot be suspicious
 * - "NO" otherwise
 *
 * Strategy
 * - Treat consecutive repeats as one letter
 * - Store it in a character set. If we ever encounter another letter down the line, output "NO"
 * - If we complete the string without outputting "NO", then output "YES"
 */

#include<iostream>
#include <string>
#include <unordered_set>


void solve(){
    int length {0};
    std::string tasks;
    std::cin >> length;
    std::cin >> tasks;

    std::unordered_set<char> seen;
    bool suspicious {false};
    for (int i=0; i<length; i++){
        if (seen.find(tasks[i]) != seen.end()) {
            suspicious = true;
            break;
        }
        while (i+1 < length && tasks[i] == tasks[i+1]) i++;
        seen.insert(tasks[i]);
    }
    if (suspicious) std::cout << "NO" << std::endl;
    else std::cout << "YES" << std::endl;

    return;

}

int main(){
    int numTestCases {0};
    std::cin >> numTestCases;
    for (int i=0; i<numTestCases; i++) solve();
    return 0;
}
