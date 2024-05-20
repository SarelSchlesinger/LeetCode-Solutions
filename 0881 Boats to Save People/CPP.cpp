// time complexity: O(n*log(n))
// space complexity: O(1)

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());
        int head = 0, tail = people.size() - 1, boats = 0;
        while (head <= tail) {
            if (people[head] + people[tail] <= limit) {
                head++;
            }
            tail--;
            boats++;
        }
        return boats;
    }
};