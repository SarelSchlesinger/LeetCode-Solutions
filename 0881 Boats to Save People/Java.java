// time complexity: O(n*log(n))
// space complexity: O(1)

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int head = 0, tail = people.length - 1, boats = 0;
        while (head <= tail) {
            if (people[head] + people[tail] <= limit) {
                head++;
            }
            tail--;
            boats++;
        }
        return boats;
    }
}