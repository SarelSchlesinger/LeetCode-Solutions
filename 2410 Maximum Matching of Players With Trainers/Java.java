// time complexity:  O(m * log(m) + n * log(n))
// space complexity: O(log(m) + log(n))

class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int res = 0, i = 0, j = 0;
        while (i < players.length && j < trainers.length) {
            if (players[i] <= trainers[j])  {
                res++;
                i++;
            }
            j++;
        }
        return res;
    }
}