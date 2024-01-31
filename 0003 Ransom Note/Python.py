class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
        return True