// time Complexity: O(n)
// space complexity: O(1)

class Solution {
    public int firstUniqChar(String s) {
        int[] frequency = new int[26];
        int[] index = new int[26];
        for (int i = 0; i < 26; i++) {
            frequency[i] = 0;
            index[i] = -1;
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            frequency[c - 'a']++;
            index[c - 'a'] = i;  
        }
        ArrayList<Integer> nums = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (frequency[i] == 1) {
                nums.add(index[i]);
            }
        }
        return nums.isEmpty() ? -1 : Collections.min(nums);
    }
}