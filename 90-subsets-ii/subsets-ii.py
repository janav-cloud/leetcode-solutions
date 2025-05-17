class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  # Sort to handle duplicates
        ans = []
        ds = []
        self.rec(0, nums, ds, ans)
        return ans

    def rec(self, i, nums, ds, ans):
        if i == len(nums):
            if ds not in ans:
                ans.append(ds[:])  # Add a copy of ds
            return
        
        self.rec(i + 1, nums, ds, ans)
        ds.append(nums[i])
        self.rec(i + 1, nums, ds, ans)
        ds.pop()