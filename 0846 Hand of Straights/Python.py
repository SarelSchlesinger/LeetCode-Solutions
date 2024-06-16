class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if groupSize == 1: return True
        if len(hand) % groupSize != 0: return False
        hand.sort(reverse=True)
        i = -1
        lastPop = j = -2
        counter = 0
        while hand:
            if counter < groupSize - 1:
                if hand[j] - hand[i] > 1:
                    return False
                elif hand[i] == lastPop:
                    i -= 1
                elif hand[i] + 1 == hand[j]:
                    lastPop = hand.pop(i)
                    j += 1
                    counter += 1
                else:
                    j -= 1
                    if -j > len(hand): return False
            else:
                lastPop = hand.pop() if lastPop + 1 == hand[-1] else hand.pop(j)
                i = -1
                lastPop = j = -2
                counter = 0
        return True