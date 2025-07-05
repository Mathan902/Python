#https://leetcode.com/problems/sum-of-squares-of-special-elements/
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        for i in range(1, len(nums)+1):
            if((len(nums)%i) == 0):
                total += nums[i-1] * nums[i-1]
        return total; 
        