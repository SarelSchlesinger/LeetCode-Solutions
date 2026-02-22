class Solution(object):
    def removeAnagrams(self, words):
        res = [words[0]]
        counter = Counter(words[0])
        for i in range(1, len(words)):
            current_counter = Counter(words[i])
            if counter != current_counter:
                res.append(words[i])
                counter = current_counter
        return res