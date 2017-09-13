# TODO: Recursive solution:
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.lol(nums, -sys.maxint - 1, 0)
        
    def lol(self, nums, prev, curpos):
        if curpos == len(nums):
            return 0
            
        taken = 0
        if prev < nums[curpos]:
            taken = 1 + self.lol(nums, nums[curpos], curpos + 1)
        
        nottaken = self.lol(nums, prev, curpos + 1)
        
        seq_len = max(taken, nottaken)
        return seq_len

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # LIS for a single element is 1
        dp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
# TODO: https://www.youtube.com/watch?v=S9oUiVYEq7E
# n lg n solution
# https://leetcode.com/problems/longest-increasing-subsequence/description/