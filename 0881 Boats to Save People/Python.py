# time complexity: O(n*log(n))
# space complexity: O(n)

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)   # using Timsort
        boats = head = 0
        tail = len(people) - 1
        while head <= tail:
            if people[head] + people[tail] <= limit:
                tail -= 1
            head += 1
            boats += 1
        return boats

