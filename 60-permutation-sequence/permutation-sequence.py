class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Compute factorial manually
        def compute_factorial(x):
            result = 1
            for i in range(2, x + 1):
                result *= i
            return result

        nums = list(range(1, n + 1))
        fact = compute_factorial(n) // n
        k -= 1
        res = []
        while nums:
            index = k // fact
            res.append(str(nums[index]))
            nums.pop(index)
            if not nums:
                break
            k %= fact
            fact //= len(nums)
        return "".join(res)