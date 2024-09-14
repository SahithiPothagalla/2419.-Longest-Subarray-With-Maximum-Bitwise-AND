class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        count = 0
        res = 0
        for i in nums:
            if i == m:
                count += 1
            else:
                count = 0
            res = max(res, count)
        return res
