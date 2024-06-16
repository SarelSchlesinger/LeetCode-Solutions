# space complexity: O(1)

class Solution(object):

    def dictionaries_intersection(self, d1, d2):
            return {i: min(d1[i], d2[i]) for i in set(d1.keys()).intersection(set(d2.keys()))}

    def commonChars(self, words):
        for i in range(len(words)):
            words[i] = Counter(words[i])
        
        intersection = reduce(self.dictionaries_intersection, words)

        return [key for key in intersection for _ in range(intersection[key])]