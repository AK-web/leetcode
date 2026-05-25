class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sol[i] = sol[i] * nums[j]
        return sol