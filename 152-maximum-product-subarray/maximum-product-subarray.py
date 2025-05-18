class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        Max = nums[0]
        Min = nums[0]
        product = nums[0]
        
        for i in range(1, n):
            curr = nums[i]

            if curr < 0:
                Max, Min = Min, Max
                
            Max = max(curr, Max * curr)
            Min = min(curr, Min * curr)
            product = max(product, Max)
        
        return product