class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        i = 0
        j = 1
        max_abs_diff = -1
        first_num = nums[0]
        n = len(nums)
        while j <= n:
            if i == n - 1:
                diff = abs(nums[i] - first_num)
            else:
                diff = abs(nums[j] - nums[i])
            if diff > max_abs_diff:
                max_abs_diff = diff
            i += 1
            j += 1
        return max_abs_diff