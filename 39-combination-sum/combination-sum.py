class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, current_sum, current_list):
            if current_sum == target:
                result.append(list(current_list))
                return
            if current_sum > target or index >= len(candidates):
                return

            # Exclude current
            backtrack(index + 1, current_sum, current_list)

            # Include current
            current_list.append(candidates[index])
            backtrack(index, current_sum + candidates[index], current_list)
            current_list.pop()  # Backtrack

        backtrack(0, 0, [])
        return result