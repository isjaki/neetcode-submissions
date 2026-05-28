class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0] * nums_len * 2

        for i in range(nums_len * 2):
            if i < nums_len:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i - nums_len]
        
        return ans
