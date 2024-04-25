# time complexity: O(n^2)

class Solution(object):
    def isValidSudoku(self, board):
        
        def isNotValid(nums):
            counter = {"1":0, "2":0 ,"3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            for i in range(len(nums)):
                if nums[i] != '.':
                    if counter[nums[i]] == 1:
                        return True
                    else:
                        counter[nums[i]] = 1
            return False
    
        for i in range(9):
            # row
            if isNotValid(board[i]): return False
            # column
            if isNotValid([board[j][i] for j in range(9)]): return False
            # box
            if isNotValid([board[i // 3 * 3 + k // 3][i % 3 * 3 + k % 3] for k in range(9)]): return False
        return True