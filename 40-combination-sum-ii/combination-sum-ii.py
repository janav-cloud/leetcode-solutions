class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # \U0001f522 Sort to group duplicates
        result = []

        def backtrack(index, target, current):
            if target == 0:
                result.append(list(current))  # ✅ Valid combination
                return
            if target < 0 or index >= len(candidates):
                return  # ❌ Prune

            # ✅ Include current
            current.append(candidates[index])
            backtrack(index + 1, target - candidates[index], current)
            current.pop()  # \U0001f519 Backtrack

            # ❌ Exclude and skip duplicates
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            backtrack(next_index, target, current)

        backtrack(0, target, [])
        return result