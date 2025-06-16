class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_diff = float('-inf')

        for num in nums:
            if num > min_val:
                max_diff = max(max_diff, num - min_val)
            else:
                min_val = num

        if max_diff == float('-inf'):
            return -1
        else:
            return max_diff