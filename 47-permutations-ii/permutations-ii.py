class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for num in nums:
            n = len(res)
            new_res = []
            for i in range(n):
                prev = res[i]
                for j in range(len(prev)+1):
                    if j > 0 and prev[j-1] == num:
                        break
                    new1 = prev[:j] + [num] + prev[j:]
                    new_res.append(new1)
            res = new_res
        return res