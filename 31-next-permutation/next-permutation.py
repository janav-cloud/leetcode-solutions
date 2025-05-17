from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        stack = []
        idx = -1
        n = len(nums)
        j = n - 2

        # Step 1: Find the pivot index where nums[j] < nums[j+1]
        while j >= 0:
            if nums[j] < nums[j + 1]:
                idx = j
                break
            else:
                stack.append(nums[j + 1])
                j -= 1

        # Step 2: If no such pivot is found, reverse to smallest permutation
        if idx == -1:
            nums.sort()
        else:
            stack.append(nums[idx + 1])
            # Step 3: Find the smallest number > nums[idx] in stack to swap
            for i in range(len(stack)):
                if stack[i] > nums[idx]:
                    stack[i], nums[idx] = nums[idx], stack[i]
                    break
            # Step 4: Sort and assign the rest
            stack.sort()
            for i in range(idx + 1, n):
                nums[i] = stack[i - (idx + 1)]