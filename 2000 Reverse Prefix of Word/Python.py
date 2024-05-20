# time complexity: O(n)
# space complexity: O(n)

class Solution(object):
    def reversePrefix(self, word, ch):
        for i in range(len(word)):
            if word[i] == ch:
                return word[i::-1] + word[i + 1:]
        return word