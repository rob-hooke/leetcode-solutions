#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp:
                return [temp[complement], i]
            temp[nums[i]] = i
        
# @lc code=end

