class Solution(object):
    def isVowel(self, s):
        return True if s in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] else False
    def halvesAreAlike(self, s):
        return len([letter for letter in s[:len(s)//2] if self.isVowel(letter)]) == len([letter for letter in s[len(s)//2:] if self.isVowel(letter)])