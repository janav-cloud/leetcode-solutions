class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        table = []
        for num in nums:
            if num in table:
                continue
            else:
                table.append(num)

        size = len(table)
        for i in range(0, n):
            if i < size:
                nums[i] = table[i]
            else:
                nums[i] = '_'

        return size