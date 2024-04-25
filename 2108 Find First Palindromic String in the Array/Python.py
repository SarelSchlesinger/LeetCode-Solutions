class Solution(object): 
    def firstPalindrome(self, words):
        
        def isPalindrome(word):
            while len(word) > 1:
                if word[0] == word[-1]:
                    word = word[1:-1]
                else: return False
            return True

        for word in words:
            if isPalindrome(word): return word
        return ""
        