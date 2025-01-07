class Solution(object):
    def countSeniors(self, details):
        counter = 0
        for person in details:
            if ord(person[11]) > 54 or (ord(person[11]) == 54 and ord(person[12]) > 48):
                counter += 1
        return counter